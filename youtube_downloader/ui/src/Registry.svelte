<script lang="ts">
	let url: string|null = null;
	import RegistryGroup from "./RegistryGroup.svelte";
	import RegistryItem from "./RegistryItem.svelte";
	import groupByDate, { dateFromGroup } from "./Registry.utils";


	export let isInSelectionMode = false;
	export let data: (TItem & {selected: boolean})[] = [];
	$: groupedData = groupByDate(data);
	$: keys = Object.keys(groupedData).sort((a,b)=>groupedData[a][0].created - groupedData[b][0].created);


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
{#each keys as key (key)}
<RegistryGroup data={dateFromGroup(groupedData[key])}>
	{#each groupedData[key] as item (item.id)}
	<RegistryItem data={item} {isInSelectionMode} on:selectionChange={forward}/>
	{/each}
</RegistryGroup>
{/each}

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