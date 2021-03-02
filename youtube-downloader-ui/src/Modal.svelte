<script>
    export let visible = false;
    import { createEventDispatcher } from "svelte";
    
    const dispatch = createEventDispatcher();
</script>

<div class={`modal ${visible ? 'modal--show' : ''}`}>
    <div class="modal__content">
        <h3>Modal Dialog</h3>
        <div>
            <p>This is a modal window. You can do the following things with it:</p>
            <ul>
                <li><strong>Read:</strong> modal windows will probably tell you something important so don't forget to read what they say.</li>
                <li><strong>Look:</strong> a modal window enjoys a certain kind of attention; just look at it and appreciate its presence.</li>
                <li><strong>Close:</strong> click on the button below to close the modal.</li>
            </ul>
            <button class="modal__close" on:click={()=>dispatch("closeModal", null)}>Close me!</button>
        </div>
    </div>
</div>
<div class="modal__overlay"></div><!-- the overlay element -->

