const thumbnailURLFromFileName = (filename) => `http://youtube.downloader.local/thumbnails/${filename}`
const getDefaultResolution = (streams) => Object.keys(streams).find(key => streams[key] == streams["default"] && key !== "default")



export {
    thumbnailURLFromFileName,
    getDefaultResolution
}