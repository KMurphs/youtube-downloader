export type TMenuItem = {
    id: string|number,
    leftSlot: string,
    rightSlot: string,
    hasSubMenu: boolean,
    onClick: (evt: MouseEvent) => void
}
export interface TMenuStore {
    getItems: (node: HTMLElement) => TMenuItem[]
} 

export type TCoordinates = {x: number, y: number}