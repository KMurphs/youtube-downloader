import { TMenuStore } from "./menu.types";

let id = 0;
const getId = ()=>id++;


const menuStore: TMenuStore = {
  getItems: (node: HTMLElement)=>[
    { id: getId(), onClick: (evt)=> console.log(1), hasSubMenu: false, leftSlot: "View Item", rightSlot: "<i class='fas fa-ellipsis-v'></i>" },
    { id: getId(), onClick: (evt)=> console.log(1), hasSubMenu: false, leftSlot: "Edit Item", rightSlot: "<i class='fas fa-ellipsis-v'></i>" },
  ]
}

export default menuStore;