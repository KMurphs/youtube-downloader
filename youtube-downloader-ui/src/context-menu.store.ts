import type { TMenuStore } from "./context-menu.types";

let id = 0;
const getId = ()=>id++;


const menuStore: TMenuStore = {
  getItems: (node: HTMLElement)=>[
    { id: getId(), onClick: (evt)=> console.log(1), hasSubMenu: false, leftSlot: "View Item", rightSlot: "<i class='fas fa-eye'></i>" },
    { id: getId(), onClick: (evt)=> console.log(2), hasSubMenu: false, leftSlot: "Edit Item", rightSlot: "<i class='fas fa-pencil-alt'></i>" },
    { id: getId(), onClick: (evt)=> console.log(3), hasSubMenu: false, leftSlot: "Select Item", rightSlot: "<i class='fas fa-hand-pointer'></i>" },
  ]
}

export default menuStore;