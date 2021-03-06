<script lang="ts">
	import Icon from "./Icon.svelte";
	let url: string|null = null;
</script>

<section class="group">
	
	<a href="#1" class={`reset group__thumbnail ${url ? '' : 'group__thumbnail--placeholder'}`}>
		{#if url}
			<img  class="" src="" alt="">
		{:else}
			<i class="fas fa-video-slash"></i>
		{/if}
	</a>
	<div class="group__title-block">
		<h1 class="group__title">title</h1>
		<h2 class="group__subtitle">Author</h2>
		<div class="group__keywords"><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span></div>
	</div>
	<div class="group__more">
		<Icon extraClass="icon--option no-box-shadow--important hover:bg-dark-5--important scale-up-10" faClass="fa-ellipsis-v "/>
	</div>

</section>

<style>
.group{
	display: flex;
	align-items: stretch;
	padding: .5rem .5rem;
	padding-right: 0;
	transition: background-color .3s ease-in-out, border-color .3s ease-in-out;
	border-left: 2px solid transparent;
}
.group__more{
	margin-left: auto;
	align-self: center;
}
.group__thumbnail{
	/* height: 100%; */
	min-height: 2rem;
	width: 3rem;
	display: flex;
	justify-content: center;
	align-items: center;
	border: 1px solid #bbb;
	margin-right: .5rem;
}
.group:hover{
	background-color: rgba(0,0,0,0.03);
	border-color: rgba(0,0,0,0.5)
}
.group__title{
	font-size: 1rem;
}
.group__subtitle{
	font-size: .8rem;
	line-height: 1;
}
.group__keywords{
	display: none;
    flex-wrap: wrap;
}
@media screen and (min-width: 640px){
	.group{
		padding: 1rem 1rem;
	}
	.group__thumbnail{
		/* height: 100%; */
		min-height: 4rem;
		width: 6rem;
		margin-right: 1rem;
	}
	.group__title{
		font-size: 1.2rem;
	}
	.group__subtitle{
		font-size: 1rem;
	}
	.group__keywords{
		display: flex;
	}
}
.group__keyword{
	font-size: .8rem;
	margin-right: .4rem;
	font-style: italic;
}
</style>