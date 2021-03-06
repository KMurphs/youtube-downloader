<!-- <script context="module">
    let counter = 0
	const getId = ()=>counter++;
	const itemId = `item-checkbox-${getId()}`;
</script> -->

<script lang="ts">
	import Icon from "./Icon.svelte";
	import { longpress } from './longpress';
	let url: string|null = null;

	export let data: TItemExtended;
	const {id, title, author, keywords} = data;
	$: itemId = `item-checkbox-${id}`;



	import { createEventDispatcher } from "svelte";
	import type { TItemExtended } from "./App.types";
	export let isInSelectionMode = false;
	let isSelected = false;
	
	const dispatch = createEventDispatcher();
	const hanldeSelectionChange = ()=>{
		isSelected = !isSelected;
		dispatch("selectionChange", {id: id, state: isSelected});
	}
</script>





<section class="group" use:longpress on:longpress={e => (isInSelectionMode = true) && hanldeSelectionChange()}>
	{#if isInSelectionMode}
	<label for={itemId} class="group__checkbox">
		<input type="checkbox" id={itemId} checked={isSelected} on:change={hanldeSelectionChange}>
	</label>
	{/if}
	<a href="#1" class={`reset group__thumbnail ${url ? '' : 'group__thumbnail--placeholder'}`}>
		{#if url}
			<img  class="" src="" alt="">
		{:else}
			<i class="fas fa-video-slash"></i>
		{/if}
	</a>
	<div class="group__title-block">
		<h1 class="group__title">{title}</h1>
		<h2 class="group__subtitle">{author}</h2>
		<div class="group__keywords">
			{#each keywords.split(", ") as keyword}
			<span class="group__keyword">{keyword}</span>
			{/each}
		</div>
	</div>
	<div class="group__more has-menu">
		<Icon extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-ellipsis-v "/>
	</div>

</section>

<style>
.group{
	display: flex;
	align-items: stretch;
	padding: .5rem .5rem;
	padding-right: 0;
	transition: background-color .3s ease-in-out, border-color .3s ease-in-out;
	border-left: 2px solid transparent;
}
.group__more{
	margin-left: auto;
	align-self: center;
}
.group__thumbnail{
	/* height: 100%; */
	min-height: 2rem;
	width: 3rem;
	display: flex;
	justify-content: center;
	align-items: center;
	border: 1px solid #bbb;
	margin-right: .5rem;
}
.group:hover{
	background-color: rgba(0,0,0,0.03);
	border-color: rgba(0,0,0,0.5)
}
.group__title{
	font-size: 1rem;
}
.group__subtitle{
	font-size: .8rem;
	line-height: 1;
}
.group__keywords{
	display: none;
    flex-wrap: wrap;
}
@media screen and (min-width: 640px){
	.group{
		padding: 1rem 1rem;
	}
	.group__thumbnail{
		/* height: 100%; */
		min-height: 4rem;
		width: 6rem;
		margin-right: 1rem;
	}
	.group__title{
		font-size: 1.2rem;
	}
	.group__subtitle{
		font-size: 1rem;
	}
	.group__keywords{
		display: flex;
	}
}
.group__keyword{
	font-size: .8rem;
	margin-right: .4rem;
	font-style: italic;
}
.group__checkbox{
	/* outline: 1px solid red; */
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 0 1rem 0 0;
}
</style>