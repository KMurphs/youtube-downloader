<script lang="ts">
	export let name: string;
	import Icon from "./Icon.svelte";
</script>

<nav class="app-nav">
	<ul class="reset">
		<li><Icon faClass="fa-info"/></li>
		<li><Icon faClass="fa-bars"/></li>
		<li><Icon faClass="fa-plus"/></li>
		<li><Icon faClass="fa-home"/></li>
	</ul>
</nav>

<style>
.app-nav{
	position: absolute;
	right: 2rem;
	bottom: 2rem;
}

</style>