<script lang="ts">
	import Icon from "./Icon.svelte";
	let url: string|null = null;
</script>

<section class="group">
	
	<aside class="group__date">16<br><span class="group__text--muted">Oct</span></aside>


	<!-- Video title, author, thumbnail and link -->
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


	<!-- More Details about current video length, keywords -->
	<input type="checkbox" id="toggle-details">
	<footer class="group__details">
		<div class="group__keywords"><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span><span class="group__keyword">keyword</span></div>
		<div class="group__misc-details">
			<span class="">214 <span class="group__text--muted">sec</span></span>
			<span class="group__detail-label group__text--muted">Downloaded at:</span>
			<span class="">2021-02-13 15:14:23</span>
		</div>
	</footer>
	

	<!-- Controls for the ui group/component -->
	<aside class="group__options">
		<label for="toggle-details"><Icon extraClass="icon--option" faClass="fa-angle-up"/></label>
		<Icon extraClass="icon--option" faClass="fa-pen"/>
		<!-- <Icon extraClass="icon--option" faClass="fa-search"/> -->
	</aside>


</section>

