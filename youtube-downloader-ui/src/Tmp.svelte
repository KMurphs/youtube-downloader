<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);
</script>



<h3>Modal Dialog</h3>
<div>
    <p>This is a modal window. You can do the following things with it:</p>
    <ul>
        <li><strong>Read:</strong> modal windows will probably tell you something important so don't forget to read what they say.</li>
        <li><strong>Look:</strong> a modal window enjoys a certain kind of attention; just look at it and appreciate its presence.</li>
        <li><strong>Close:</strong> click on the button below to close the modal.</li>
    </ul>
</div>
<div>
    <button on:click={closeModal}>Close me!</button>
</div>




<style>

h3 {
	margin: 0;
	padding: 0.4em;
	text-align: center;
	font-size: 2.4em;
	font-weight: 300;
	opacity: 0.8;
	background: rgba(0,0,0,0.1);
	border-radius: 3px 3px 0 0;
}

div {
	padding: 15px 40px 30px;
	margin: 0;
	font-weight: 300;
	font-size: 1.15em;
}

p {
	margin: 0;
	padding: 10px 0;
}

ul {
	margin: 0;
	padding: 0 0 30px 20px;
}

ul li {
	padding: 5px 0;
}

button {
	display: block;
	margin: 0 auto;
	font-size: 0.8em;
}
</style>