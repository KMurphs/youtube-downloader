<script lang="ts">
import getId from "./InputWithMovingLabel.utils";
import { createEventDispatcher } from "svelte";


/**
 * Typing documented here: https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/typescript.md#typing-component-events
 */
const dispatchKeyDown = createEventDispatcher<{

	keydown: KeyboardEvent
}>();

export let type = "text";
export let value: string|number = "";
export let label = "Some Label";
export let disabled = false;
export let extraClasses = "";

const id = getId()
</script>


<section class={`input-with-moving-label ${disabled ? 'input-with-moving-label--disabled' : ''} ${extraClasses}`} >
	{#if type === "textarea"}
	<textarea name={`textarea-${id}`}
			id={`${id}`}
			rows=5
			required 
			disabled={disabled}
			bind:value={value} 
			on:keydown={e=>dispatchKeyDown("keydown", e)}
	/>
	{:else if type === "text"}
	<input id={`${id}`} 
			type="text"
			required 
			disabled={disabled}
			bind:value={value} 
			on:keydown={e=>dispatchKeyDown("keydown", e)}
	/>
	{:else}
	<input id={`${id}`} 
			type="number"
			required 
			disabled={disabled}
			bind:value={value} 
			on:keydown={e=>dispatchKeyDown("keydown", e)}
	/>
	{/if}

	<label for={`${id}`} class="moving-label">{label}</label>
</section>



<style>
.input-with-moving-label {
  	/* Styling container */
	position: relative;
	padding-top: 1.5rem;
	display: grid;
	grid-template: 1fr / 1fr;
	margin-top: .5rem;
}

.input-with-moving-label .moving-label,
.input-with-moving-label input,
.input-with-moving-label textarea{
	/* Position children on the grid */
	grid-area: 1 / 1 / 2 / 2;
	position: relative;
}

.input-with-moving-label .moving-label{
	/* Style for original position of label */
	padding-left: .5rem;
	padding-top: .5rem;
	top: 0;
	left: 0;
	color: #777;
}
.input-with-moving-label input,
.input-with-moving-label textarea{
  	/* General styles for the input */
	z-index: 1;
	background: none !important;

	padding: .5rem .5rem;
    line-height: 1;
    outline: none;
    border: none;
    border-bottom: 1px solid red;
    border-bottom: 1px solid var(--accent-2, red);
}
.input-with-moving-label *{
  	/* General styles for the input */
  	transition: top .3s, left .3s, font-size .3s;
} 

.input-with-moving-label input:disabled ~ .moving-label,
.input-with-moving-label input:valid ~ .moving-label,
.input-with-moving-label input:focus ~ .moving-label,
.input-with-moving-label textarea:disabled ~ .moving-label,
.input-with-moving-label textarea:valid ~ .moving-label,
.input-with-moving-label textarea:focus ~ .moving-label{
	/* Style for label displayed on top */
	top: -2rem;
	top: -1.5rem;
	left: -1rem;
	left: -0.5rem;
	font-size: .8rem;
}
.input-with-moving-label.input-with-moving-label--disabled{
	background-color: #0000002e;
}
</style> 