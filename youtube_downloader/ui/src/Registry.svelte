<script lang="ts">
	let url: string|null = null;
	import RegistryGroup from "./RegistryGroup.svelte";
	import RegistryItem from "./RegistryItem.svelte";
	import groupByDate, { dateFromGroup } from "./Registry.utils";


	export let isInSelectionMode = false;
	export let data: (TItem & {selected: boolean})[] = [];
	$: groupedData = groupByDate(data);
	$: keys = Object.keys(groupedData).sort((a,b)=>groupedData[a][0].added_at - groupedData[b][0].added_at);


	import { createEventDispatcher } from 'svelte';
	import type { TItem } from "./App.types";

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
{:then data}
	{#each keys as key (key)}
	<RegistryGroup data={dateFromGroup(groupedData[key])}>
		{#each groupedData[key] as item (item.id)}
		<RegistryItem data={item} {isInSelectionMode} on:selectionChange={forward}/>
		{/each}
	</RegistryGroup>
	{/each}
{:catch error}
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