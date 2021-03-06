<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import Icon from "./Icon.svelte";
	export let isInSelectionMode: boolean;
	const dispatch = createEventDispatcher();
</script>

<header class="app-header">
	<h1>Videos</h1>
	<div class="app-header__search-input">
		<input type="text" placeholder="Enter text to filter displayed items">
		<Icon extraClass="icon--image position-absolute r-2" faClass="fa-search"/>
	</div>
</header>

<div class={`app-selection-controls ${isInSelectionMode ? 'visible' : 'hidden'}`}>
	<button on:click={()=>dispatch("selectionControlAction", "select-all")}>Select All</button>
	<button on:click={()=>dispatch("selectionControlAction", "select-none")}>Deselect All</button>
	<button on:click={()=>dispatch("selectionControlAction", "cancel")}>Cancel</button>
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
}
.app-selection-controls button{
	padding: .2rem .5rem;
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
</style>