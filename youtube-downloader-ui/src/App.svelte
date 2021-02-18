<script lang="ts">
	export let name: string;
</script>

<div class="app-container">
	<header>My header</header>
	<main>My Main Section</main>
	<nav>My nav</nav>
</div>

<style>

.app-container{
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	background-color: #eee;
	position: relative;
	z-index: 10;
	/* border-radius: 15px; */
}

@media screen and (min-width: 1441px){
	.app-container {
		/* top: 19px; */
		width: 1396px;
		height: calc(100% - 38px);
	}
}


</style>