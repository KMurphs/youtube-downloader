<script lang="ts">
	// import Icon from "./Icon.svelte";
	// let url: string|null = null;
	const [day, month]: [number, string] = [16, "Oct"]
</script>

<section class="group">
	<aside class="group__date">
		<span class="group__day">{day}</span>
		<span class="group__month">{month}</span>
	</aside>
	<slot></slot>	
</section>


<style>
	.group{
		margin-left: 2.5rem;
		position: relative;
		padding-top: 1rem;
		padding-left: 1rem;
		padding-bottom: 3rem;
	}
	.group::before{
		position: absolute;
		content: "";
		border-radius: 50%;
		z-index: 10;
		background-color: #fff;
		width: 1rem;
		height: 1rem;
		left: -.5rem;
		top: 1rem;
		--size: 1rem;
		width: var(--size);
		height: var(--size);
		left: calc(var(--size) / -2);
		top: var(--size);
		border: 4px solid blue;
	}
	.group::after{
		position: absolute;
		content: "";
		background-color: blue;
		width: 1px;
		left: 0;
		top: 1.5rem;
		bottom: -1.5rem;
	}
	.group__date{
		display: flex;
		flex-direction: column;
		position: absolute;
		left: -2.5rem;
		line-height: 1rem;
		top: 0;
	}
	.group__day{
		color: #333;
		font-weight: bold;
	}
	.group__month{
		color: #333;
	}
</style>
