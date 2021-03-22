<script lang="ts">
    import { createEventDispatcher, onMount } from "svelte";
	import type { TItem } from "./App.types";
	import Icon from "./Icon.svelte";
	import AddItem from "./AddItem.svelte";
	import { thumbnailURLFromFileName, getDefaultResolution } from "./App.utils";
    const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);
	// export let data: TItem;
</script>



<h3 class="content__header">Add Video Items</h3>

<div class="content__wrapper">
	<AddItem />
</div>

<div class="content__footer">
    <button on:click={closeModal} class="btn btn-primary">Close</button>
</div>




<style>

h3 {
	margin: 0;
	padding: 0.4em;
	text-align: center;
	font-size: 1.5rem;
	font-weight: 300;
	opacity: 0.8;
	background: rgba(0,0,0,0.1);
	border-radius: 3px 3px 0 0;
}


.content__wrapper, .content__header, .content__footer{
	padding: 1rem 2rem;
	min-width: auto;
}

.badge{
	display: inline-block;
    padding: 0.3rem 0.7rem;
    margin: 0 2px;
    /* border: 1px solid rgb(222, 189, 189); */
    border-radius: 18px;
    line-height: 1;
    font-size: .9rem;
	display: inline-block;
    padding: .25em .4em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .25rem;
    color: #212529;
    background-color: #e2f0ff;
}
.badge--active{
    color: #fff;
    background-color: #dc3545;
}
/* .badge--small{
	padding: 2px 8px;
	font-size: .8rem;
} */
.content__footer{
	display: flex;
	justify-content: center;
}
h4{
	font-weight: bold;
	line-height: 1.5;
	font-size: 1.2rem;
	margin-top: 1rem;
}
h4 .badge{
	position: relative;
	top: -2px;
}

h4 a .link-icon{
	opacity: 0;
}
h4 a:hover .link-icon{
	opacity: 1;
}
h5{
	line-height: 1;
	font-size: 1rem;
	margin: 0rem 0 1rem 0;
	display: flex;
	justify-content: space-between;
}
h5 .author::before{
	content: "By ";
}
h5 .length::after{
	content: " sec";
}
img{
	margin: 1rem auto;
	display: block;
	width: 100%;
	box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
p{
	margin: 1rem 0; 
}

.dates .text-muted{
	display: inline-block;
	width: 95px;
}
</style> 