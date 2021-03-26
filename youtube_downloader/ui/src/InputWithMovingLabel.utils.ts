const getId = ()=>Date.now() + "-" + Math.random().toPrecision(16).split(".")[1]

export default getId;