// export type TItem = {
//     id: string, 
//     title: string, 
//     author: string, 
//     thumbnail: string, 
//     created: number, 
//     keywords: string,
// }


export type TItem = {
    id: string, 
    title: string,
    author: string,
    length: number,
    keywords: string[],
    tags: string[],
    uri: string,
    uri_hash: string,
    watch_url: string,
    thumbnail_url:string,
    thumbnail_filepath: string,
    thumbnail_filename: string,
    streams: { [key: string]: number },
    status: number,
    video_filename: string,
    video_filepath: string,
    added_at: number,
    added_at_str: string,
    completed_at: number|null,
    completed_at_str: string|null
}
export type TItemExtended = TItem & {date: number, month: string, year: number}
export type TRegisterData = {[key: string]: (TItemExtended & {selected: boolean})[]}