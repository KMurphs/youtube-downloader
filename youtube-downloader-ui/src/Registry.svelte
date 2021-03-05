<script lang="ts">
	let url: string|null = null;
	import RegistryGroup from "./RegistryGroup.svelte";
	import RegistryItem from "./RegistryItem.svelte";
	// export let name: string;
</script>

<main class="registry">
<RegistryGroup>
		<RegistryItem/>
		<RegistryItem/>
		<RegistryItem/>
	</RegistryGroup>
	<RegistryGroup>
		<RegistryItem/>
		<RegistryItem/>
		<RegistryItem/>
	</RegistryGroup>
	<RegistryGroup>
		<RegistryItem/>
		<RegistryItem/>
		<RegistryItem/>
	</RegistryGroup>
</main>

<style>


.registry{
    margin-top: 1rem;
    padding-top: 3rem;
    overflow-y: auto;
}
</style>