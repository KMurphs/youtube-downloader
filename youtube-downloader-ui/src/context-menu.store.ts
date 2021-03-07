import type { TMenuStore } from "./context-menu.types";

const removeSpecialChars = (str: string): string => str.replace(/[^a-zA-Z0-9 ]/g, " ")
const camelize = (str: string): string => {
  return str.toLowerCase().replace(/(?:^\w|[A-Z]|\b\w|\s+)/g, function(match, index) {
    if (+match === 0) return ""; // or if (/\s+/.test(match)) for white spaces
    return index === 0 ? match.toLowerCase() : match.toUpperCase();
  });
}
const bubbleToDataAttributeOwner = (node: HTMLElement, dataAttributeName: string): string|null => {
  // From the origin of the event, climb up the chain
  // until we either find a dom element with the camelized data attribute "dataAttributeName" 
  // (then return the value of that data attribute)
  // or we get to the root of all dom elements (the window - in which case return null) 
  // let currNode: HTMLElement = (evt.srcElement || evt.target) as HTMLElement;
  let currNode: HTMLElement = node;
  const attributeName = camelize(removeSpecialChars(dataAttributeName));
  while(currNode){
    if(currNode.dataset && attributeName in currNode.dataset) 
      return currNode.dataset[attributeName];
    currNode = currNode.parentNode as HTMLElement;
  }

  return null;
}


let id = 0;
const getId = ()=>id++;

const getMenuStore = (dataIDAttributeName, onSelectItem): TMenuStore => {
  
  return { 
    getItems: (node: HTMLElement)=>{
      const id = bubbleToDataAttributeOwner(node, dataIDAttributeName);
      return [
        { id: getId(), onClick: (evt)=> console.log(1), hasSubMenu: false, leftSlot: "View Item", rightSlot: "<i class='fas fa-eye'></i>" },
        { id: getId(), onClick: (evt)=> console.log(2), hasSubMenu: false, leftSlot: "Edit Item", rightSlot: "<i class='fas fa-pencil-alt'></i>" },
        { id: getId(), onClick: (evt)=> onSelectItem(id), hasSubMenu: false, leftSlot: "Select Item", rightSlot: "<i class='fas fa-hand-pointer'></i>" },
      ]
    }
  }
}


export default getMenuStore;