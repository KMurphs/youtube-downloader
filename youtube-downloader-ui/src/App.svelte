<script lang="ts">
	// export let name: string;
	import { onMount } from "svelte";
	import Nav from "./Nav.svelte";
	import Header from "./Header.svelte";
	import Registry from "./Registry.svelte";
	import Tmp from "./Tmp.svelte";
	import Modal from "./Modal.svelte";
	import defineVH from "./vh";
	import withMenu from "./context-menu";
	import getMenuStore from "./context-menu.store";
	import _data from "./data";
	import type { TItem } from "./App.types";
	onMount(defineVH);
	
	

	let isModalShowing = false;

	let data: (TItem & {selected: boolean})[] | null = null;
	
	const loadData = ()=> {
		console.log("Loading data");
		data = _data.map(item => ({...item, selected: false}))
	};
	if(!data) loadData();

	let isInSelectionMode = false;
	const handleSelectionChangeFromMenu = (itemId)=>handleSelectionChange({itemId, state: data.filter(({id}) => id === itemId)[0].selected})
	const handleSelectionChange = ({itemId, state})=>{
		isInSelectionMode = true;
		data = data.map(({selected, id, ...rest}) => (id === itemId ? {selected: !state, id, ...rest} : {selected, id, ...rest}));
	}
	const handleSelectionControlAction = ({detail}) => {
		(detail === "select-all") && (data = data.map(({selected, ...rest}) => ({selected: true, ...rest})));
		(detail === "select-none" || detail === "cancel") && (data = data.map(({selected, ...rest}) => ({selected: false, ...rest})));
		(detail === "cancel") && (isInSelectionMode = false);
	}
	onMount(()=>withMenu(document.querySelector(".app-container"), getMenuStore("id-menu-owner", handleSelectionChangeFromMenu)));
</script>

<Modal visible={isModalShowing} on:closeModal={()=>(isModalShowing = false)}>
	<Tmp on:closeModal={()=>(isModalShowing = false)}/>
</Modal>

<div class="app-container">
	<Header   {isInSelectionMode}        on:selectionControlAction={handleSelectionControlAction}/>
	<Registry {isInSelectionMode} {data} on:selectionChange={({detail})=>handleSelectionChange(detail)}/>
	<Nav on:sidePanelOpen={()=>(isModalShowing=true)}/>
</div>

<style>


.app-container{
	width: 100%;
	/* height: 100%; */
	height: 100vh; /* Fallback for browsers that do not support Custom Properties */
	height: calc(var(--vh, 1vh) * 100);
	display: flex;
	/* padding: 2rem; */
	flex-direction: column;
	justify-content: flex-start;
	align-items: stretch;
	background-color: #F5F6FA;
	position: relative;
	z-index: 10;
	box-shadow: 0 1px 1px 0 rgba(0,0,0,.06),0 2px 5px 0 rgba(0,0,0,.2);
}

@media screen and (min-width: 1441px){
	.app-container {
		width: 1396px;
		/* height: calc(100% - 38px); */
	}
}




</style>