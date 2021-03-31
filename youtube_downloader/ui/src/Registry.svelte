<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import type { TVideo } from "./App.types";

	
	import RegistryGroup from "./RegistryGroup.svelte";
	import RegistryItem from "./RegistryItem.svelte";
	import groupByDate, { dateFromGroup } from "./Registry.utils";


	export let isInSelectionMode = false;
	export let data: (TVideo & {selected: boolean})[] = [];
	$: groupedData = groupByDate(data);
	$: keys = Object.keys(groupedData).sort((a,b)=>groupedData[a][0].added_at - groupedData[b][0].added_at);




	const dispatch = createEventDispatcher();
	const forward = ({type, detail}) => dispatch(type, detail);
</script>

<!-- <script context="module">
    let counter = 0
	const getId = ()=>counter++;
	const itemId = `item-checkbox-${getId()}`;
</script> -->

<main class="registry">

{#await data}
	<p>...waiting</p>
{:then}
	{#each keys as key (key)}
	<RegistryGroup data={dateFromGroup(groupedData[key])}>
		{#each groupedData[key] as item (item.id)}
		<RegistryItem data={item} {isInSelectionMode} on:selectionChange={forward}/>
		{/each}
	</RegistryGroup>
	{/each}
{:catch}
	<p>An error occurred!</p>
{/await}




</main>

<style>


.registry{
    margin-top: 1rem;
	padding: 1rem;
	padding-right: 0;
    /* padding-top: 3rem; */
    overflow-y: auto;
	flex: 1 1 auto;
}
@media screen and (min-width: 640px){
	.registry {
		padding: 2rem;
	}
}

</style>