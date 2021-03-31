<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import Icon from "./Icon.svelte";
	import { fly } from 'svelte/transition';
	const dispatch = createEventDispatcher();


	export let isInSelectionMode: boolean;
	let show = false
	$: isInSelectionMode && setTimeout(()=>(show = true), 200);
	$: !isInSelectionMode && (show = false);


	export let filterExpression = "";


	export let downloadLink: string  = null;
	
</script>

<header class="app-header">
	<h1>Videos</h1>
	<div class="app-header__search-input">
		<input type="text" placeholder="Enter text to filter displayed items" bind:value={filterExpression}>
		<Icon extraClass="icon--image position-absolute r-2" faClass="fa-search"/>
	</div>
</header>

<div class={`app-selection-controls ${isInSelectionMode ? 'visible' : ''} ${show ? 'app-selection-controls--show' : ''}`}>
	<div class={`app-selection-controls__container`}>
		<span class="">
			<button class="btn btn-outline-primary" on:click={()=>dispatch("selectionControlAction", "select-all")}>Select All</button>
			<button class="btn btn-outline-primary" on:click={()=>dispatch("selectionControlAction", "select-none")}>Deselect All</button>
			<button class="btn btn-outline-primary" on:click={()=>dispatch("selectionControlAction", "cancel")}>Cancel</button>
		</span>
		<span class="">
			<button class="btn btn-primary" on:click={()=>dispatch("selectionControlAction", "download")}>Zip Files</button>
			{#if downloadLink}
			<a href={downloadLink} class="btn btn-outline-primary" transition:fly="{{ x: 200, duration: 400 }}">Download</a>
			{/if}
		</span>
	</div>
	
</div>

<style>
.app-header{
	flex: 0 0 auto;
	padding: .5rem 1rem;
}
@media screen and (min-width: 640px){
	.app-header {
		padding: 2rem;
	}
}
.app-header__search-input{
	display: flex;
	align-items: center;
	flex-wrap: wrap;
	justify-content: space-between;
	position: relative;
}

input{
	outline: none;
	border: none;
	width: 100%;
	font-size: 1rem;
	line-height: 1.5;
	padding: .5rem 1rem;
	padding-right: 3rem;
	border-radius: 3px;
}

::-webkit-input-placeholder { /* Chrome/Opera/Safari */
	font-size: .9rem;
	/* letter-spacing: .1px; */
	color: #aaa;
}
::-moz-placeholder { /* Firefox 19+ */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}
:-ms-input-placeholder { /* IE 10+ */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}
:-moz-placeholder { /* Firefox 18- */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}
.app-selection-controls{
	display: flex;
	justify-content: space-between;
	padding: .5rem 1rem;
	display: none;
	visibility: hidden;
	-webkit-backface-visibility: hidden;
	-moz-backface-visibility: hidden;
	backface-visibility: hidden;
}
.app-selection-controls__container{
	-webkit-transform: translateX(20%);
	-moz-transform: translateX(20%);
	-ms-transform: translateX(20%);
	transform: translateX(20%);
	opacity: 0;
	-webkit-transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
	-moz-transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
	transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
	display: flex;
	justify-content: space-between;
	width: 100%;
}
.app-selection-controls.visible{
	display: flex;
}
.app-selection-controls.app-selection-controls--show{
	visibility: visible;
	-webkit-backface-visibility: visible;
	-moz-backface-visibility: visible;
	backface-visibility: visible;
}
.app-selection-controls.app-selection-controls--show .app-selection-controls__container{
	-webkit-transform: translateX(0);
	-moz-transform: translateX(0);
	-ms-transform: translateX(0);
	transform: translateX(0);
	opacity: 1;
}
.app-selection-controls button{
	padding: .2rem 2rem;
	font-size: .8rem;
}
@media screen and (min-width: 640px){
	.app-selection-controls{
		padding: 0rem 2rem;
		justify-content: flex-start;
	}
	.app-selection-controls button{
		margin-right: .5rem;
	}
}
.btn-primary{
	background-color: var(--primary);
	border-color: var(--primary);
}
.btn-primary:hover{
	background-color: var(--primary--darker);
	border-color: var(--primary);
}
a.btn{
	min-height: 40px;
	color: var(--primary);
	display: inline-block;
	border: 1px solid var(--primary);
    padding: .2rem 1.5rem;
    font-size: .8rem;
    line-height: 2rem;
}
a.btn:hover{
	background-color: var(--primary);
	color: white;
}

</style>