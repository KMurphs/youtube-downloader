<script lang="ts">
	let url: string|null = null;
	import RegistryGroup from "./RegistryGroup.svelte";
	import RegistryItem from "./RegistryItem.svelte";


	export let isInSelectionMode = false;
	export let data: TRegisterData = {};
	const keys = Object.keys(data).sort((a,b)=>data[a][0].created - data[b][0].created);
	const getGroupData = (data: TItemExtended): [number, string, number] => ([data.date, data.month, data.year])


	import { createEventDispatcher } from 'svelte';
	import type { TItemExtended, TRegisterData } from "./App.types";

	const dispatch = createEventDispatcher();
	const forward = ({type, detail}) => dispatch(type, detail);
</script>

<script context="module">
    let counter = 0
	const getId = ()=>counter++;
	const itemId = `item-checkbox-${getId()}`;
</script>

<main class="registry">
{#each keys as key (key)}
<RegistryGroup data={getGroupData(data[key][0])}>
	{#each data[key] as item (item.id)}
	<RegistryItem bind:data={item} bind:isInSelectionMode on:selectionChange={forward}/>
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