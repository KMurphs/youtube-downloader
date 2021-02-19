<script lang="ts">
	export let faClass: string = "fa-download";
	export let faBase: string = "fas";
	export let extraClass: string = "icon--btn";
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
	background-color: transparent;
	transition: box-shadow .3s;
}

.icon.icon--btn{
	cursor: pointer;
	background-color: #eee;
	box-shadow: 0 1px 1px 0 rgba(0,0,0,.06),0 2px 5px 0 rgba(0,0,0,.2);
}
.icon.icon--btn:hover{
	box-shadow: 0 2px 2px 0 rgba(0,0,0,.06),0 4px 10px 0 rgba(0,0,0,.2);
}
.icon.icon--image{
	height: 100%;
	width: auto;
}
.icon.icon--option{
	cursor: pointer;
	width: 2rem;
	height: 2rem;
	margin: .25rem;
}
.icon.icon--option:hover{
	box-shadow: 0 1px 1px 0 rgba(0,0,0,.06),0 2px 5px 0 rgba(0,0,0,.2);
}

</style>