<script lang="ts">
	// export let name: string;
	import Nav from "./Nav.svelte";
	import Header from "./Header.svelte";
	import Registry from "./Registry.svelte";
	import Modal from "./Modal.svelte";

	let isModalShowing = false;
</script>

<Modal visible={isModalShowing} on:closeModal={()=>(isModalShowing = false)}/>

<div class="app-container">
	<Header/>
	<Registry/>
	<!-- <Nav on:sidePanelOpen={()=>(isSidePanelShowing=true)}/> -->
	<Nav on:sidePanelOpen={()=>(isModalShowing=true)}/>
</div>

<style>

.app-container{
	width: 100%;
	height: 100%;
	display: flex;
	padding: 2rem;
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
		height: calc(100% - 38px);
	}
}




</style>