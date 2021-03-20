import type { TItem, TItemExtended, TRegisterData } from "./App.types";

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
const groupByDate = (data: (TItem & {selected: boolean})[]): TRegisterData => {
    return data.reduce((acc, item)=>{
        const {date, month, year} = dateMonthYearFromTimeStamp(item.added_at)
        const key = dateMonthYearToKey({date, month, year});
        if(!(key in acc)) acc[key] = [];
        acc[key].push({...item, date, month, year});
        return acc;
    }, {} as TRegisterData);
} 
export const dateFromGroup = ([data]: TItemExtended[]): [number, string, number] => ([data.date, data.month, data.year])
export default groupByDate;