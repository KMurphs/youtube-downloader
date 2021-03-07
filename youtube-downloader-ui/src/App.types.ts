export type TItem = {
    id: string, 
    title: string, 
    author: string, 
    thumbnail: string, 
    created: number, 
    keywords: string,
}
export type TItemExtended = TItem & {date: number, month: string, year: number}
export type TRegisterData = {[key: string]: (TItemExtended & {selected: boolean})[]}