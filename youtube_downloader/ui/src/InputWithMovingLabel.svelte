<script lang="ts">
export let type = "text";
export let value = "";
export let label = "Some Label";
</script>


<section class="input-with-moving-label" >
	{#if type === "textarea"}
	<textarea name="textarea-1"
			id="textarea-1" 
			required 
			value={value} 
			on:change={()=>{/*evt => setValue((evt.target as HTMLInputElement).value)*/}}
	/>
	{:else}
	<input id="input-1" 
			type={type} 
			required 
			value={value} 
			on:change={()=>{/*evt => setValue((evt.target as HTMLInputElement).value)*/}}
	/>
	{/if}

	<label for="input-1" class="moving-label">{label}</label>
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
}
.input-with-moving-label *{
  	/* General styles for the input */
  	transition: top .3s, left .3s, font-size .3s;
} 

.input-with-moving-label input:valid ~ .moving-label,
.input-with-moving-label input:focus ~ .moving-label,
.input-with-moving-label textarea:valid ~ .moving-label,
.input-with-moving-label textarea:focus ~ .moving-label{
	/* Style for label displayed on top */
	top: -2rem;
	top: -1.5rem;
	left: -1rem;
	left: -0.5rem;
	font-size: .8rem;
}
</style> 