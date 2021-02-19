<script lang="ts">
	let url: string|null = null;
	// import Icon from "./Icon.svelte";
	// export let name: string;
</script>

<main>
	<section class="group">
		<span class="group__date">16<br><span class="group__text--muted">Oct</span></span>
		<div>
			<a href="#1">
				{#if url}
					<img src="" alt="">
				{:else}
					<span><i class="fas fa-video-slash"></i></span>
				{/if}
			</a>
			<span>title</span>
		</div>
		<div><span>keywords</span><span>author, length, completed at</span></div>
	</section>
</main>

<style>
.group{
	position: relative;
	padding-left: 2rem;
	margin-left: 2.5rem;
}
.group::before{
	content: "";
    display: block;
    position: absolute;
    left: -.25px;
    top: 0;
    bottom: 0;
    height: 100%;
    width: .5px;
    background-color: #d4d5d8;
}
.group::after{
	--size: 12px;
    content: "";
    display: block;
    position: absolute;
    left: -5px;
    left: calc(-1 * var(--size)/2);
    top: -5px;
    top: calc(-1 * var(--size)/2);
    top: 0;
	width: 10px;
    width: var(--size);
    height: 10px;
    height: var(--size);
    border: 3.1px solid red;
    border-radius: 50%;
    background-color: #eee;
}
.group__date{
	position: absolute;
	left: -2.5rem;
	line-height: 1;
	font-size: .8rem;
	font-weight: bold;
}
.group__text--muted{
	color: #9e9fa3;
	font-size: .8rem;
	font-weight: bold;
}
</style>