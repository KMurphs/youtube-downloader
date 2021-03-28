<script lang="ts">
    import { createEventDispatcher } from "svelte";
	import type { TVideo } from "./App.types";
	import Icon from "./Icon.svelte";
	import { thumbnailURLFromFileName } from "./api.interface";
	import { getDefaultResolution } from "./Form.utils";
    const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);
	export let data: TVideo;
</script>



<h3 class="content__header">View Video Item</h3>

<div class="content__wrapper">
	{#if data}
	<h4>
		<a href={data.watch_url} rel="noopener noreferrer" target="_blank" class="mr-2">
			<span class="mr-1 font-bold">{data.title}</span> 
			<span class="link-icon"><Icon extraClass="icon--image p-0--important m-0--important font-normal" faClass="fa-link "/></span> 
		</a> 
		<span class={`badge badge--small ${data.status > 0 ? "badge--active" : ""}`}>{data.status > 0 ? "Downloaded" : "Scheduled"}</span>
	</h4>
	<img src={thumbnailURLFromFileName(data.thumbnail_filename)} alt="">
	<h5>
		<span class="author">{data.author}</span>
		<span class="length">{data.length}</span>
	</h5>
	<p>
		<span class="text-muted">Resolution: </span>
		{#each Object.keys(data.streams).filter(key=>key!=="default") as key}
		<span class={`${getDefaultResolution(data.streams) === key ? "badge--active": ""} badge`}>{key}</span>
		{/each}
	</p>
	<p class="d-flex justify-between flex-column dates">
		<span class="mt-2"><span class="text-muted">Added At: </span>{data.added_at_str}</span>
		<span class="mt-2"><span class="text-muted">Completed At: </span>{data.completed_at_str?data.completed_at_str:""}</span>
	</p>
	
	<p class="">
		<span class="tags-keywords text-muted">Tags and keywords:</span>	
		{#each data.tags as tag}
		<span class="badge badge--small">{tag}</span>
		{/each}
		{#each data.keywords as keyword}
		<span class="badge badge--small">{keyword}</span>
		{/each}
	</p>
	{/if}
</div>

<div class="content__footer">
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
/* .badge--small{
	padding: 2px 8px;
	font-size: .8rem;
} */
.content__footer{
	display: flex;
	flex-direction: column;
	justify-content: center;
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
p{
	margin: 1rem 0; 
}

.dates .text-muted{
	display: inline-block;
	width: 95px;
}
</style> 