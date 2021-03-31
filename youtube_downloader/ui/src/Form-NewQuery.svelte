<script lang="ts">
    import { createEventDispatcher } from "svelte";
	import InputWithMovingLabel from "./InputWithMovingLabel.svelte";
	import { submitQuery } from "./api.interface";
	import type { TVideo } from "./App.types";
	import { allowTabInTextArea } from "./Form.utils"
    const dispatchCloseModal = createEventDispatcher<{closeModal: null}>();
    const dispatchResults = createEventDispatcher<{queryResults: TVideo[]}>();
    const closeModal = () => dispatchCloseModal("closeModal", null);
    const queryAPI = (data: TVideo[]) => dispatchResults("queryResults", data);
	
	let query_string: string = "{}";
	let query_object: {[key: string]: any}|null = {};

	$: query_object = ((json_string)=>{
		try{ return JSON.parse(json_string) }
		catch(e){ return null }
	})(query_string)


</script>



<h3 class="content__header">Submit New Query</h3>

<div class="content__wrapper">
	<InputWithMovingLabel label="DSL Query" type="textarea" bind:value={query_string} on:keydown={(e)=>allowTabInTextArea(e.detail)} extraClasses="math"/>
	<div class={`is-valid-json ${query_object ? '' : 'is-valid-json--invalid'}`}>
		{#if !!query_object }
		Valid JSON Object
		{:else }
		Invalid JSON Object
		{/if}
	</div>
</div>

<div class="content__footer">
    <button on:click={()=>closeModal && submitQuery(query_object || {}, null, queryAPI)} class="btn btn-primary">Submit</button>
    <button on:click={closeModal} class="btn btn-outline-primary">Close</button>
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


button{
	width: 100%;
    margin-top: 1rem;
}



.content__footer{
	display: flex;
	flex-direction: column;
	justify-content: center;
}

.is-valid-json{
    margin-top: .5rem;
    background-color: #a4e7a4;
    padding: .5rem;
    font-size: .8rem;
    color: #005b00;
    font-weight: bold;
	transition: background-color .3s ease-in-out, color .3s ease-in-out;
}
.is-valid-json--invalid{
    background-color: #ffd8d8;
    color: red;
}


:global(.math textarea) {
	font-family: 'math', 'Courier New', Courier, monospace;
}
</style> 