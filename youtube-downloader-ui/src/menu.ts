import { TCoordinates, TMenuItem, TMenuStore } from './menu.types';

// TODO: Modify menu placement function "moveNodeTo" to handle placing submenus






const bubbleToClassOwner = (evt: MouseEvent, className: string): HTMLElement|null => {
  // From the origin of the event, climb up the chain
  // until we either find a dom element with class "className" (then return said element)
  // or we get to the root of all dom elements (the window - in which case return null) 
  let currNode: HTMLElement = (evt.srcElement || evt.target) as HTMLElement;
  while(currNode){
    if(currNode.classList && currNode.classList.contains(className)) 
      return currNode;
    currNode = currNode.parentNode as HTMLElement;
  }

  return null;
}



const translateCoords = (from: TCoordinates, by: TCoordinates): TCoordinates => ({x: from.x + by.x, y: from.y + by.y}) 
const getClickCoordinates = (clickEvt: MouseEvent): TCoordinates => {
  
  const [posX, posY] = (function(evt: MouseEvent){
    if (evt.pageX || evt.pageY) return [evt.pageX, evt.pageY];
    if (evt.clientX || evt.clientY) return [
      evt.clientX + document.body.scrollLeft + document.documentElement.scrollLeft,
      evt.clientY + document.body.scrollTop + document.documentElement.scrollTop
    ];
    return [0, 0];
  })((clickEvt || window.event) as MouseEvent)

  return { x: posX, y: posY }
}



const fitObjectInFrame = (objPos: number, objSize: number, frameSize: number): number => {
  // Try placing menu at between position and frame far end, 
  if((objPos + objSize) < frameSize) return objPos;
  // then between frame start and position,  
  if((objPos - objSize) > 0) return objPos - objSize;
  // then the closest to frame far end border
  return frameSize - objSize;
}


const moveNodeTo = (node: HTMLElement, where: TCoordinates) => {
  
  // Get window width and height
  const {innerWidth: windowWidth, innerHeight: windowHeight} = window;
 
  // Increase width and height of node by a small margin
  const margin = 4;
  const nodeWidth = node.offsetWidth + margin;
  const nodeHeight = node.offsetHeight + margin;
  
  // Move the node to [x, y] unless overflow (in which case don't go behond max coords)
  node.style.left = `${fitObjectInFrame(where.x, nodeWidth, windowWidth)}px`;
  node.style.top = `${fitObjectInFrame(where.y, nodeHeight, windowHeight)}px`;
}


const buildUpMenuItem = (
  classMenuPane: string, 
  classSubMenuSrc: string, 
  { id, leftSlot, rightSlot, hasSubMenu, onClick }: TMenuItem): HTMLElement => {
  
  const item = document.createElement("li");
  item.setAttribute("class",`${classMenuPane}__item ${hasSubMenu ? classSubMenuSrc : ''}`);
  item.setAttribute("data-menu-item-id",`${id}`);
  item.innerHTML = `<span>${leftSlot}</span><span>${rightSlot}</span>`;
  
  // Make sure to remove any listeners that might come with left and right slots
  const itemClone = item.cloneNode(true);
  // Add our own listener
  onClick && itemClone.addEventListener("click", onClick);
  
  return (itemClone as HTMLElement);
};



const bringUpMenu = (
  {x, y}: TCoordinates, 
  items: TMenuItem[], 
  classMenuSrc: string, 
  classSubMenuSrc: string) => {
  
  const classMenuPane = "context-menu";
  
  // list embedded in menu/nav
  const list = document.createElement("ul");
  
  // Manufacture a menu "nav.context-menu > ul > li"
  const menu = document.createElement("nav");
  menu.classList.add(classMenuPane);
  menu.appendChild(list);
  document.body.append(menu);

  const bringDownMenu = () => document.body.contains(menu) && document.body.removeChild(menu);
  const bringDownMenuHOF = (f: Function) => f && ((...args) => { bringDownMenu(); f(...args); });
  
  // Prepare the menu items
  items.map(({onClick, ...rest}) => ({...rest, ...{"onClick": bringDownMenuHOF(onClick)}}))
       .map(buildUpMenuItem.bind(null, classMenuPane, classSubMenuSrc))
       .forEach(list.appendChild);
  
  // Move menu to some position while preventing overflows ...
  moveNodeTo(menu, {x, y});

  // Return function to cleanup/remove menu from DOM
  return bringDownMenu;
}


const withMenu = (root: HTMLElement, menuStore: TMenuStore, classMenuSrc = "has-menu", classSubMenuSrc = "has-submenu") => {
  /* Closure to limit scopes of cleanup function here */
  let cleanupMenu: Function|null = null;

  root.addEventListener("click", (evt)=>{
    
    // By default, after every click anywhere in root, remove menu if displayed
    evt.preventDefault();
    cleanupMenu && cleanupMenu();
    
    // Did we click inside a node that needs a menu?
    const menuNode = bubbleToClassOwner(evt, classMenuSrc);
    
    // We did. Get Menu items, and build up the menu around click coords
    menuNode && menuStore && menuStore.getItems && (
      cleanupMenu = bringUpMenu(
      getClickCoordinates(evt), 
      menuStore.getItems(menuNode), 
      classMenuSrc,
      classSubMenuSrc
    ));
    
  })
  
  return root;
}

// withMenu(document.querySelector(".container"), menuStore);
// withMenu(document, menuStore);
export default withMenu;
  
