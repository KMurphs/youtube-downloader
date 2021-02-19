<script lang="ts">
	import Icon from "./Icon.svelte";
	let url: string|null = null;
</script>

<section class="group">
	<aside class="group__date">16<br><span class="group__text--muted">Oct</span></aside>
	<header class="group__header">
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
		</div>
	</header>
	<footer><span>keywords</span><span>author, length, completed at</span></footer>
	<aside class="group__options">
		<Icon extraClass="icon--option" faClass="fa-search"/>
		<Icon extraClass="icon--option" faClass="fa-search"/>
		<Icon extraClass="icon--option" faClass="fa-search"/>
	</aside>
</section>

<style>
.group{
	position: relative;
	padding-left: 2rem;
	padding-right: .5rem;
	margin-left: 2.5rem;
	padding-top: 1rem;
	padding-bottom: 1rem;
	background-color: transparent;
	transition: background-color .3s;
	display: grid;
	grid-template: auto 1fr / 1fr auto;
}
.group:hover{
	background-color: rgba(0, 0, 0, .05);
}
.group::before{
	content: "";
    display: block;
    position: absolute;
    left: -.25px;
    top: 0;
	top: 1rem;
    bottom: 0;
    height: 100%;
    width: .5px;
    background-color: #d4d5d8;
}
.group:last-child::before{ height: calc(100% - 1rem); }
.group::after{
	--size: 12px;
    content: "";
    display: block;
    position: absolute;
    left: -5px;
    left: calc(-1 * var(--size)/2);
    top: -5px;
    top: calc(-1 * var(--size)/2);
    top: 1rem;
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

.group__thumbnail{
	display: inline-grid;
	width: 10rem;
	min-height: 7rem;
	grid-template: 1fr / 1fr;
	margin-right: 1rem;
	transition: box-shadow .3s;
}
.group__thumbnail i{
	font-size: 3rem;
	margin: auto;
}
.group__thumbnail--placeholder{
	height: 100%;
	border: 1px solid #d4d5d8;
}
.group__thumbnail:hover{
	box-shadow: 0 2px 2px 0 rgba(0,0,0,.06),0 4px 10px 0 rgba(0,0,0,.2);
	box-shadow: 0 1px 1px 0 rgba(0,0,0,.06),0 2px 5px 0 rgba(0,0,0,.2);
}
.group__header{
	display: flex;
	align-items: stretch;
	position: relative;
	padding-right: .5rem;
}
.group__subtitle{
	font-size: .8rem;
}
.group__options{
	display: flex;
	flex-direction: column;
	grid-area: 1 / 2 / 3 / 3;
}
.group__title-block{
	flex: 1 0 0;
}
</style>