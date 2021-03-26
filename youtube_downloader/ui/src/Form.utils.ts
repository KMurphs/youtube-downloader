import type { TSubmission, TVideo } from "./App.types"

export type TItem = TSubmission & { status: ""|"success"|"failure"|"fetching" }

const getDefaultResolution = (streams) => Object.keys(streams).find(key => streams[key] == streams["default"] && key !== "default")


const classFromStatus = (status: string) => ["success","failure"].includes(status) ? `item-to-add--${status}` : ""
export {
	classFromStatus,
	getDefaultResolution
}