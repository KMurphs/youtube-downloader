<script lang="ts">
	let url: string|null = null;
	import RegistryItem from "./RegistryItem.svelte";
	// export let name: string;
</script>

<main class="registry">
	<RegistryItem/>
	<RegistryItem/>
	<RegistryItem/>
</main>

<style>


.registry{
    margin-top: 1rem;
    padding-top: 3rem;
    overflow-y: auto;
}
</style>