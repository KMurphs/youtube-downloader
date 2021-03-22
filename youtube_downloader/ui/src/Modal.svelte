<script>
    export let visible = false;
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    const closeModal = () => dispatch("closeModal", null);
</script>

<div class={`modal ${visible ? 'modal--show' : ''}`}>
    <div class="modal__content">
        <slot></slot>
    </div>
</div>
<div class="modal__overlay" on:click={closeModal}></div><!-- the overlay element -->







<style>

/* Base Styles */
.modal {
	position: fixed;
	top: 0;
	right: 0;
	bottom: 0;
	/* width: 50%; */
	/* width: 30%; */
	width: 400px;
	/* max-width: 630px; */
	max-width: 100%;
	min-width: 320px;
	z-index: 2000;
	visibility: hidden;
	-webkit-backface-visibility: hidden;
	-moz-backface-visibility: hidden;
	backface-visibility: hidden;
}

.modal__overlay {
	position: fixed;
	width: 100%;
	height: 100%;
	visibility: hidden;
	top: 0;
	left: 0;
	z-index: 1000;
	opacity: 0;
	background: rgba(143,27,15,0.8);
	-webkit-transition: all 0.3s;
	-moz-transition: all 0.3s;
	transition: all 0.3s;
}













/* Content styles */
.modal__content {
	color: #fff;
	background: #f2f8ff;
	position: relative;
	border-radius: 3px;
	margin: 0 auto;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	overflow-y: auto;
}




























.modal .modal__content {
	-webkit-transform: translateX(20%);
	-moz-transform: translateX(20%);
	-ms-transform: translateX(20%);
	transform: translateX(20%);
	opacity: 0;
	-webkit-transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
	-moz-transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
	transition: all 0.3s cubic-bezier(0.25, 0.5, 0.5, 0.9);
}

.modal.modal--show {
	visibility: visible;
}

.modal.modal--show .modal__content {
	-webkit-transform: translateX(0);
	-moz-transform: translateX(0);
	-ms-transform: translateX(0);
	transform: translateX(0);
	opacity: 1;
}

.modal.modal--show ~ .modal__overlay {
	opacity: 1;
	visibility: visible;
    background: #638ab836;
}




</style>
