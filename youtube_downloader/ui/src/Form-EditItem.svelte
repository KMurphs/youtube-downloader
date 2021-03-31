<script lang="ts">
    import { createEventDispatcher } from "svelte";
	import Icon from "./Icon.svelte";
	import InputWithMovingLabel from "./InputWithMovingLabel.svelte";
	import { submitLinks, thumbnailURLFromFileName } from "./api.interface";
	import { getDefaultResolution } from "./Form.utils";
	import type { TItem } from "./Form.utils";
	import type { TVideo } from "./App.types";
	import "./test.css"


	const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);

	
	let currentItem: TItem = {url: "", resolution: 720, tags: "", status: ""}
	
	export let video: TVideo;
	$: currentItem = {url: video.watch_url, resolution: parseInt(getDefaultResolution(video.streams)+""), tags: video.tags.join(","), status: ""}

	let data: TItem[] = []
	const loadAsCurrentItem = (url="", resolution=720, tags="")=>(currentItem = {url, resolution, tags, status: ""})
	const addNewItem = () => {data = [...data.filter(item => currentItem.url !== item.url), {...currentItem}]; loadAsCurrentItem()}
	// const removeItem = (url) => (data = data.filter(item => url !== item.url))
	// onMount(()=>data=[{"url": "https://www.youtube.com/watch?v=7IS7gigunyI", "resolution": 720, "tags":"nginx", "status":""}])


	const submit = ()=>submitLinks(
		data.map(({tags, ...rest}) => ({...rest, tags: tags.split(",")})),
		()=>data = data.map(({status, ...rest}) => ({...rest, status: "fetching"})),
		(failed: string[], created: string[])=>{
			failed.forEach(item => data = data.map(({status, ...rest}) => ({...rest, status: rest.url.includes(JSON.parse(item).video.uri) ? "failure" : status})))
    		created.forEach(item => data = data.map(({status, ...rest}) => ({...rest, status: rest.url.includes(JSON.parse(item).video.uri) ? "success" : status})))
		}
	)
	
	
</script>



<h3 class="content__header">Edit Video Items</h3>

<section class="form">	
	<h4>Enter Video Details: </h4>
	<InputWithMovingLabel disabled label="Youtube Link" bind:value={currentItem.url}/>
	<InputWithMovingLabel disabled label="Resolution in pixels (720)" type="number" bind:value={currentItem.resolution}/>
	<InputWithMovingLabel label="Comma Separated Tags" bind:value={currentItem.tags}/>
	<button class="btn btn-primary btn-accent-2" on:click={addNewItem}>Add</button>
</section>




<div class="content__wrapper">
	{#if data}
	<h4>
		<a href={video.watch_url} rel="noopener noreferrer" target="_blank" class="mr-2">
			<span class="mr-1 font-bold">{video.title}</span> 
			<span class="link-icon"><Icon extraClass="icon--image p-0--important m-0--important font-normal" faClass="fa-link "/></span> 
		</a> 
		<span class={`badge badge--small ${video.status > 0 ? "badge--active" : ""}`}>{video.status > 0 ? "Downloaded" : "Scheduled"}</span>
	</h4>
	<img src={thumbnailURLFromFileName(video.thumbnail_filename)} alt="">
	<h5>
		<span class="author">{video.author}</span>
		<span class="length">{video.length}</span>
	</h5>
	{/if}
</div>




<div class="content__footer">
    <button on:click={closeModal} class="btn btn-outline-primary">Close</button>
</div>




<style>

h3 {
	margin: 0;
	padding: 0.4em;
	text-align: center;
	font-size: 1.5rem;
	font-weight: 300;
	opacity: 0.8;
	background: rgba(0,0,0,0.1);
	border-radius: 3px 3px 0 0;
}


.content__wrapper, .content__header, .content__footer{
	padding: 1rem 2rem;
	min-width: auto;
}
.content__wrapper{
	flex-grow: 1;
}
.content__footer{
	display: flex;
	flex-direction: column;
}
.form{ 
	transform: scale(.9);
	/* background-color: #f2f8ff; */
	border-radius: 5px;
	padding: 1rem;
	padding-top: 0;
}

button{
	width: 100%;
    margin-top: 1rem;
}
h4{
	font-weight: bold;
	line-height: 1.5;
	font-size: 1.2rem;
	margin-top: 1rem;
}
h4 .badge{
	position: relative;
	top: -2px;
}

h4 a .link-icon{
	opacity: 0;
}
h4 a:hover .link-icon{
	opacity: 1;
}
h5{
	line-height: 1;
	font-size: 1rem;
	margin: 0rem 0 1rem 0;
	display: flex;
	justify-content: space-between;
}
h5 .author::before{
	content: "By ";
}
h5 .length::after{
	content: " sec";
}
img{
	margin: 1rem auto;
	display: block;
	width: 100%;
	box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.badge{
	display: inline-block;
    padding: 0.3rem 0.7rem;
    margin: 0 2px;
    /* border: 1px solid rgb(222, 189, 189); */
    border-radius: 18px;
    line-height: 1;
    font-size: .9rem;
	display: inline-block;
    padding: .25em .4em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .25rem;
    color: #212529;
    background-color: #e2f0ff;
}
.badge--active{
    color: #fff;
    background-color: #dc3545;
    background-color: #6E356E;
}
h4 .badge{
	position: relative;
	top: -2px;
}

</style> 