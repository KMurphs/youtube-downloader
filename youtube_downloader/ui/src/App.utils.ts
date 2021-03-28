import type { TVideo } from "./App.types";

const removeCharsFromEnds = (str: string, charsToRemove: string = "[]") => {
	const _removeCharsFromEnds = (s, chars, currChar, start, end) => {
		if(currChar < 0) return s.substring(start, end - start + 1);
		if(start >= end) _removeCharsFromEnds(s, chars, -1, 0, -1);
		return _removeCharsFromEnds(s, chars, currChar - 1, start + (s[start] === chars[currChar] ? 1 : 0), end - (s[end] === chars[currChar] ? 1 : 0))
	}
	return _removeCharsFromEnds(str, charsToRemove, charsToRemove.length - 1, 0, str.length - 1)
}
function *filterIterator(expression: string){
	const it = expression.match(/[^\]\[]+/gm);
	for(let exp of it || [expression]){
		const [key, value] = exp.split(":");
		yield value && value.length > 0 ? [key, value] : ["any", key];
	}
}
const applyFilterExpression = (data: (TVideo & {selected: boolean})[], filterExpression: string)=>{
	
	let newData = data;
	for(let [key, value] of filterIterator(filterExpression)){
		newData = newData.filter(item => JSON.stringify(key === 'any' ? item : item[key]).toLowerCase().includes((value + "").toLowerCase()));	}
	return newData;
}

export default applyFilterExpression