import type { TSubmission, TVideo } from "./App.types"

export type TItem = TSubmission & { status: ""|"success"|"failure"|"fetching" }

const getDefaultResolution = (streams) => Object.keys(streams).find(key => streams[key] == streams["default"] && key !== "default")
const classFromStatus = (status: string) => ["success","failure"].includes(status) ? `item-to-add--${status}` : ""



const allowTabInTextArea = function(e: KeyboardEvent) {
	// https://stackoverflow.com/questions/6637341/use-tab-to-indent-in-textarea
	const src = e.currentTarget;
	if (e.key == 'Tab') {
		e.preventDefault();
		var start = (src as HTMLTextAreaElement).selectionStart;
		var end = (src as HTMLTextAreaElement).selectionEnd;

		// set textarea value to: text before caret + tab + text after caret
		(src as HTMLTextAreaElement).value = (src as HTMLTextAreaElement).value.substring(0, start) +
		"\t" + (src as HTMLTextAreaElement).value.substring(end);

		// put caret at right position again
		(src as HTMLTextAreaElement).selectionStart =
		(src as HTMLTextAreaElement).selectionEnd = start + 1;
	}
}

export {
	classFromStatus,
	getDefaultResolution,
	allowTabInTextArea
}