

const API_BASE_URL = "http://youtube.downloader.local"
const API_URL = `${API_BASE_URL}/api`
const SUBMIT_VIDEOS_URI = "/videos/new/bulk"
const SUBMIT_VIDEOS_TO_DOWNLOADS = "/zip"
const SUBMIT_QUERY = "/videos/queries"
const GET_ALL_VIDEOS_URI = "/videos/"

async function submitLinks (data: any[], preCallback: Function, postCallback: Function) {
    preCallback && preCallback();
    
    const res = await fetch(`${API_URL}${SUBMIT_VIDEOS_URI}`, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    
    const result = await res.json();
    const {failed, created} = result.results;

    postCallback && postCallback(failed, created);
}

async function submitDownloads (data: any[], preCallback: Function, postCallback: Function) {
    preCallback && preCallback();
    
    const res = await fetch(`${API_URL}${SUBMIT_VIDEOS_TO_DOWNLOADS}`, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    
    const result = await res.json();
    const {link} = result.results;
    // const link = await new Promise(resolve => setTimeout(()=>resolve("1234"), 2000));

    postCallback && postCallback(link || null);
}

async function submitQuery (query: {[key: string]: any}, preCallback: Function, postCallback: Function) {
    preCallback && preCallback();
    
    const res = await fetch(`${API_URL}${SUBMIT_QUERY}`, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },

        // { "query": { "bool": {"filter": [{ "term":  { "status": "0" }}]}	}}
        body: JSON.stringify("query" in query ? query : {query})
    });
    

    const result = await res.json();
    const {video, videos} = await result.json();

    postCallback && postCallback([video].concat(videos));
}

async function fetchAllVideos (preCallback: Function, postCallback: Function) {
    preCallback && preCallback();
    
    const res = await fetch(`${API_URL}${GET_ALL_VIDEOS_URI}`)
    const {video, videos} = await res.json();

    postCallback && postCallback([video].concat(videos));
}
const thumbnailURLFromFileName = (filename) => `${API_BASE_URL}/thumbnails/${filename}`

export { submitLinks, thumbnailURLFromFileName, fetchAllVideos, submitQuery, submitDownloads }