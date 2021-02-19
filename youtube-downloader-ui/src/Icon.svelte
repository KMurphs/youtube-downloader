<script lang="ts">
	export let faClass: string = "fa-download";
	export let faBase: string = "fas";
	export let extraClass: string = "";
</script>

<span class={`icon ${extraClass}`}>
	<!-- TODO: Add Tooltip -->
	<i class={`${faBase} ${faClass}`}></i>
</span>


<style>
.icon{
	display: inline-flex;
	justify-content: center;
	align-items: center;
	border-radius: 50%;
	width: 3rem;
	height: 3rem;
	margin: .5rem;
	background-color: #eee;
	cursor: pointer;
	transition: box-shadow .3s;
	box-shadow: 0 1px 1px 0 rgba(0,0,0,.06),0 2px 5px 0 rgba(0,0,0,.2);
}
.icon:hover{
	box-shadow: 0 2px 2px 0 rgba(0,0,0,.06),0 4px 10px 0 rgba(0,0,0,.2);
}
.icon.icon--inline{
	box-shadow: none !important;
	height: 100%;
	width: auto;
	background-color: transparent !important;
}
</style>