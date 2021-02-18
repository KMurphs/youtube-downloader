<script lang="ts">
	import Icon from "./Icon.svelte";
	export let name: string;
</script>

<header class="app-header">
	<input type="text" placeholder="Enter text to filter displayed items">
	<Icon extraClass="icon--inline position-absolute r-2" faClass="fa-search"/>
</header>

<style>
.app-header{
	display: flex;
	align-items: center;
	justify-content: space-between;
	position: relative;
	margin-bottom: 1rem;
}

input{
	outline: none;
	border: none;
	width: 100%;
	font-size: 1rem;
	line-height: 1.5;
	padding: .5rem 1rem;
	padding-right: 3rem;
	border-radius: 3px;
}

::-webkit-input-placeholder { /* Chrome/Opera/Safari */
	font-size: .9rem;
	letter-spacing: .1px;
	color: #aaa;
}
::-moz-placeholder { /* Firefox 19+ */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}
:-ms-input-placeholder { /* IE 10+ */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}
:-moz-placeholder { /* Firefox 18- */
	font-size: .9rem;
	letter-spacing: .1px;
  	color: #aaa;
}

</style>