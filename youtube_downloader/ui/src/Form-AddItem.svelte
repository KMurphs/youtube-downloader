<script lang="ts">
    import { createEventDispatcher, onMount } from "svelte";
	import Icon from "./Icon.svelte";
	import InputWithMovingLabel from "./InputWithMovingLabel.svelte";
	import CSSLoader from "./css-loaders.svelte";
	import { submitLinks } from "./api.interface";
	import type { TItem } from "./Form.utils";
	import { classFromStatus } from "./Form.utils";


	const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);

	
	let currentItem: TItem = {url: "", resolution: 720, tags: "", status: ""}
	let data: TItem[] = []
	const loadAsCurrentItem = (url="", resolution=720, tags="")=>(currentItem = {url, resolution, tags, status: ""})
	const addNewItem = () => {data = [...data.filter(item => currentItem.url !== item.url), {...currentItem}]; loadAsCurrentItem()}
	const removeItem = (url) => (data = data.filter(item => url !== item.url))
	// onMount(()=>data=[{"url": "https://www.youtube.com/watch?v=7IS7gigunyI", "resolution": 720, "tags":"nginx", "status":""}])


	const submit = ()=>submitLinks(
		data.map(({tags, ...rest}) => ({...rest, tags: tags.split(",")})),
		()=>data = data.map(({status, ...rest}) => ({...rest, status: "fetching"})),
		(failed, created)=>{
			failed.forEach(item => data = data.map(({status, ...rest}) => ({...rest, status: rest.url.includes(JSON.parse(item).video.uri) ? "failure" : status})))
    		created.forEach(item => data = data.map(({status, ...rest}) => ({...rest, status: rest.url.includes(JSON.parse(item).video.uri) ? "success" : status})))
		}
	)
	
	
</script>



<h3 class="content__header">Add Video Items</h3>

<section class="form">	
	<h4>Enter Video Details: </h4>
	<InputWithMovingLabel label="Youtube Link" bind:value={currentItem.url}/>
	<InputWithMovingLabel label="Resolution in pixels (720)" type="number" bind:value={currentItem.resolution}/>
	<InputWithMovingLabel label="Comma Separated Tags" bind:value={currentItem.tags}/>
	<button class="btn btn-primary btn-accent-2" on:click={addNewItem}>Add</button>
</section>

<div class="content__wrapper">
	{#if data.length > 0}
	<h4 class="mb-4">Items to Submit: </h4>
	{/if}
	{#each data as {url, resolution, tags, status}}
	<section class={`item-to-add ${classFromStatus(status)}`}>

		<div class="item-to-add__header">
			<a href={url} class="font-bold">{url}</a>
			<span class="icons ml-4">
				<Icon on:click={()=>loadAsCurrentItem(url, resolution, tags)} extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-edit"/>
				<Icon on:click={()=>removeItem(url)} extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-trash"/>
			</span>
		</div>
		<div class="item-to-add__status">
			{#if status === ""}
			<span></span>
			{:else if status === "fetching"}
			<CSSLoader type="ellipsis" extraClasses="loader"/>
			{:else if status === "success"}
			<Icon extraClass="icon--image" faClass="fa-check"/>
			{:else if status === "failure"}
			<Icon extraClass="icon--image" faClass="fa-times"/>
			{/if}
		</div>
		<div class="item-to-add__details">
			<span class="text-muted">{resolution ? `${resolution}p` : ""}</span>
			<span class="text-muted"> - </span>
			{#each tags.split(",") as tag}
			<span class="text-muted">{tag}</span>
			{/each}
		</div>

		
	</section>
	{/each}
</div>

<div class="content__footer">
    <button on:click={submit} class="btn btn-primary">Submit</button>
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
.item-to-add{
	border-bottom: 1px solid #ccc;
	padding: .5rem;
	display: grid;
	grid-template: 1fr auto / auto 1fr;
	transition: background-color .3s ease-in-out;
}
.item-to-add.item-to-add--success {
	background-color: #9be6ac;
}
.item-to-add.item-to-add--failure {
	background-color: #f5d7d7;
}
.item-to-add__header{
	grid-area: 1 / 1 / 2 / 3;
}
.item-to-add__status{
	display: flex;
	justify-content: flex-start;
	align-items: center;
}
.item-to-add__details{
	display: flex;
	align-items: center;
}
.item-to-add .icons{
	opacity: 0;
}
.item-to-add:hover{
	background-color: rgba(0,0,0,0.03);
}
.item-to-add.item-to-add--success:hover {
	background-color: #7fd091;
}
.item-to-add.item-to-add--failure:hover {
	background-color: #e9c8c8; 
}
.item-to-add:hover .icons{
	opacity: 1;
}
.item-to-add a:hover{
	border-bottom: 1px solid #ccc;
}
button{
	width: 100%;
    margin-top: 1rem;
}

/* https://svelte.dev/repl/765f182ddd75486a8f6cf0b3ba75f276?version=3.35.0 */
.item-to-add :global(.loader) {
    margin-bottom: -4px !important;
    margin-left: -5px !important;
    margin-right: .5rem !important;
	--size: 30px !important;
}

.item-to-add__status :global(.icon) {
	padding: 0;
    margin: 0;
    height: 1.5rem;
    border-radius: 50%;
    min-height: auto;
    width: 1.5rem;
    margin-right: 1rem;
    color: white;
}
.item-to-add__status :global(.icon *) {
    color: white;
}
.item-to-add.item-to-add--success .item-to-add__status :global(.icon) {
	background: #2a9c2a;
}
.item-to-add.item-to-add--failure .item-to-add__status :global(.icon) {
	background: #e97777; 
}
</style> 