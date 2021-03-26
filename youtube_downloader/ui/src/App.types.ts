// export type TItem = {
//     id: string, 
//     title: string, 
//     author: string, 
//     thumbnail: string, 
//     created: number, 
//     keywords: string,
// }

export type TSubmission = {
	url: string, 
	resolution: number, 
	tags: string, 
}
export type TVideo = {
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
export type TVideoExtended = TVideo & {date: number, month: string, year: number}
export type TRegisterData = {[key: string]: (TVideoExtended & {selected: boolean})[]}


export enum TModalMode {
    EMPTY     = 0,
    VIEW_ITEM = 1,
    EDIT_ITEM = 2,
    ADD_ITEM  = 3,
    NEW_QUERY = 4
}