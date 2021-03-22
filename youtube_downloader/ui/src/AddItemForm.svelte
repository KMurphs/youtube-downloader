<script lang="ts">
    import { createEventDispatcher, onMount } from "svelte";
    const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);
	import Icon from "./Icon.svelte";
	import InputWithMovingLabel from "./InputWithMovingLabel.svelte";

	type TItem = {url: string, resolution: number, tags: string}
	let currentItem: TItem = {url: "", resolution: 720, tags: ""}
	let data: TItem[] = []
	const loadCurrentItem = (url="", resolution=720, tags="")=>(currentItem = {url, resolution, tags})
	const addItem = () => {data = [...data.filter(item => currentItem.url !== item.url), {...currentItem}]; loadCurrentItem()}
	const removeItem = (url) => (data = data.filter(item => url !== item.url))
	onMount(()=>data=[{"url": "https://www.youtube.com/watch?v=7IS7gigunyI", "resolution": 720, "tags":"nginx"}])


	let result
	$: console.log({result})
	async function submitLinks () {
		console.log(JSON.stringify(data.map(({url, resolution, tags}) => ({url, resolution, tags: tags.split(",")}))))
		const res = await fetch('http://youtube.downloader.local/api/videos/new/bulk', {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data.map(({url, resolution, tags}) => ({url, resolution, tags: tags.split(",")})))
		})
		
		const json = await res.json()
		result = JSON.stringify(json)
	}
</script>



<h3 class="content__header">Add Video Items</h3>

<section class="form">	
	<InputWithMovingLabel label="Youtube Link" bind:value={currentItem.url}/>
	<InputWithMovingLabel label="Resolution in pixels (720)" type="number" bind:value={currentItem.resolution}/>
	<InputWithMovingLabel label="Comma Separated Tags" bind:value={currentItem.tags}/>
	<button class="btn btn-outline-primary" on:click={addItem}>Add</button>
</section>

<div class="content__wrapper">
	{#each data as {url, resolution, tags}}
	<section class="item-to-add">
		<a href={url} class="font-bold">{url}</a>
		<span class="icons ml-4">
			<Icon on:click={()=>loadCurrentItem(url, resolution, tags)} extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-edit"/>
			<Icon on:click={()=>removeItem(url)} extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-trash"/>
		</span>
		<br>
		<span class="text-muted">{resolution ? `${resolution}p` : ""}</span>
		<span class="text-muted"> - </span>
		{#each tags.split(",") as tag}
		<span class="text-muted">{tag}</span>
		{/each}
	</section>
	{/each}
</div>

<div class="content__footer">
    <button on:click={submitLinks} class="btn btn-primary">Submit</button>
    <button on:click={closeModal} class="btn btn-primary">Close</button>
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

.content__footer{
	display: flex;
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
}
.item-to-add .icons{
	opacity: 0;
}
.item-to-add:hover .icons{
	opacity: 1;
}
.item-to-add a:hover{
	border-bottom: 1px solid #ccc;
}
</style> 