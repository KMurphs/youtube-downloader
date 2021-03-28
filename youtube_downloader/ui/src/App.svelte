<script lang="ts">
	import { onMount } from "svelte";
	import Nav from "./Nav.svelte";
	import Header from "./Header.svelte";
	import Registry from "./Registry.svelte";
	import ViewItem from "./Form-ViewItem.svelte";
	import EditItem from "./Form-EditItem.svelte";
	import AddItem from "./Form-AddItem.svelte";
	import CustomQuery from "./Form-NewQuery.svelte";
	import Modal from "./Modal.svelte";
	import defineVH from "./vh";
	import withMenu from "./context-menu";
	import getMenuStore from "./context-menu.store";
	import type { TVideo } from "./App.types";
	import { TModalMode } from "./App.types";
	import { fetchAllVideos } from "./api.interface";
	import applyFilterExpression from "./App.utils";
	
	
	onMount(defineVH);
	


	let modalData: ({mode: TModalMode, data: string|null}) = {mode: TModalMode.EMPTY, data:null}
	const loadItemOnModal = (itemID: string, asEditable: boolean = false) => (modalData = {mode: asEditable ? TModalMode.EDIT_ITEM : TModalMode.VIEW_ITEM, data:itemID})
	const loadAddFormOnModal = () => (modalData = {mode: TModalMode.ADD_ITEM, data:null})
	const loadQueryFormOnModal = () => (modalData = {mode: TModalMode.NEW_QUERY, data:null})
	const resetModal = ()=>(modalData = {mode: TModalMode.EMPTY, data:null})
	// loadItemOnModal("_R99T3gBos2KvdxVZmXb")
	// loadAddFormOnModal()




	let data: (TVideo & {selected: boolean})[] = [];
	const loadVideos = videos => data = videos.map(item => ({...item, selected: false}))
    onMount(()=>fetchAllVideos(null, loadVideos))

	let filterExpression = "";
	$: filteredData = applyFilterExpression(data, filterExpression);



	let isInSelectionMode = false;
	const enterSelectionMode = ()=>isInSelectionMode = true
	const handleSelectionChangeFromMenu = (itemId)=>handleSelectionChange({itemId, state: data.filter(({id}) => id === itemId)[0].selected})
	const handleSelectionChange = ({itemId, state})=>{
		enterSelectionMode();
		data = data.map(({selected, id, ...rest}) => (id === itemId ? {selected: !state, id, ...rest} : {selected, id, ...rest}));
	}
	const handleSelectionControlAction = ({detail}) => {
		(detail === "select-all") && (data = data.map(({selected, ...rest}) => ({selected: true, ...rest})));
		(detail === "select-none" || detail === "cancel") && (data = data.map(({selected, ...rest}) => ({selected: false, ...rest})));
		(detail === "cancel") && (isInSelectionMode = false);
	}

	onMount(()=>withMenu(document.querySelector(".app-container"), getMenuStore("id-menu-owner", handleSelectionChangeFromMenu, loadItemOnModal)));
</script>









<Modal visible={modalData.mode !== TModalMode.EMPTY} on:closeModal={resetModal}>
	{#if modalData.mode === TModalMode.VIEW_ITEM }
	<ViewItem    on:closeModal={resetModal} data={data.filter(({id}) => id===modalData.data)[0]}/>
	{:else if modalData.mode === TModalMode.EDIT_ITEM }
	<EditItem    on:closeModal={resetModal} video={data.filter(({id}) => id===modalData.data)[0]}/>
	{:else if modalData.mode === TModalMode.ADD_ITEM }
	<AddItem     on:closeModal={resetModal}/>
	{:else if modalData.mode === TModalMode.NEW_QUERY }
	<CustomQuery on:closeModal={resetModal} on:queryResults={loadVideos}/>
	{/if}
</Modal>

<div class="app-container">
	<Header   {isInSelectionMode} bind:filterExpression={filterExpression}  on:selectionControlAction={handleSelectionControlAction}/>
	<Registry {isInSelectionMode} data={filteredData} on:selectionChange={({detail})=>handleSelectionChange(detail)}/>
	<Nav on:selectMode={enterSelectionMode} on:addItems={loadAddFormOnModal} on:newQuery={loadQueryFormOnModal}/>
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