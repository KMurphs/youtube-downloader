import type { TItem, TRegisterData } from "./App.types";

const _data: TItem[] = [
    {id: 1, title: "title 1", author: "author 1", thumbnail: "", created: 1615052705868, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 2, title: "title 2", author: "author 2", thumbnail: "", created: 1615052705868, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 3, title: "title 3", author: "author 3", thumbnail: "", created: 1615052705868, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 4, title: "title 4", author: "author 4", thumbnail: "", created: 1615052705868, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 5, title: "title 5", author: "author 5", thumbnail: "", created: 1615225540709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 6, title: "title 6", author: "author 6", thumbnail: "", created: 1615225540709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 7, title: "title 7", author: "author 7", thumbnail: "", created: 1615225540709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 8, title: "title 8", author: "author 8", thumbnail: "", created: 1615225540709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 9, title: "title 9", author: "author 9", thumbnail: "", created: 1615571140709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 10, title: "title 10", author: "author 10", thumbnail: "", created: 1615571140709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 11, title: "title 11", author: "author 11", thumbnail: "", created: 1615571140709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
    {id: 12, title: "title 12", author: "author 12", thumbnail: "", created: 1615225540709, keywords: "keyword 1, keyword 2, keyword 3, keyword 4, keyword 5"},
];

const dateMonthYearFromTimeStamp = (ts: number) => {
    const t = new Date(ts);
    return { date: t.getDate(), month: t.toLocaleString("en-us", {month: 'short'}), year: t.getFullYear() }
}
const dateMonthYearToKey = ({date, month, year}) => `${date}::${month}`;
export const keyToDateMonthYear = (key) => {
    const parts = key.split("::");
    const returnData = [ parseInt(parts[0]), parts[1] ] 
    if(parseInt(parts[2])) return [...returnData, parseInt(parts[2])]
    return returnData;
}
const groupByDate = (data: TItem[]): TRegisterData => {
    return data.reduce((acc, item)=>{
        const {date, month, year} = dateMonthYearFromTimeStamp(item.created)
        const key = dateMonthYearToKey({date, month, year});
        if(!(key in acc)) acc[key] = [];
        acc[key].push({...item, date, month, year});
        return acc;
    }, {} as TRegisterData);
} 

export default function getData(){ return groupByDate(_data) };