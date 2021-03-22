<script lang="ts">
import InputWithMovingLabel from "./InputWithMovingLabel.svelte";


</script>

<section>
	<InputWithMovingLabel label="Youtube Link"/>
	<InputWithMovingLabel label="Resolution in pixels (720)" type="number"/>
	<InputWithMovingLabel label="Comma Separated Tags"/>
</section>



<style>
section{ 
	transform: scale(.9);
	background-color: #eee;
	border-radius: 5px;
	padding: 1rem;
	padding-top: 0;
}
</style> 