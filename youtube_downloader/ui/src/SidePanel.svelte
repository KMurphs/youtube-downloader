<script lang="ts">
    import { createEventDispatcher } from "svelte";
	import { scale } from 'svelte/transition';
	import { elasticInOut } from 'svelte/easing';

    const dispatch = createEventDispatcher();

    import Icon from "./Icon.svelte";
</script>
<!-- <div transition:scale="{{duration: 500, delay: 500, opacity: 0.5, start: 0.5, easing: quintOut}}"> -->

<!-- <aside class="side-panel" in:fly="{{ x: 200, duration: 200 }}" out:fade> -->
<aside class="side-panel" transition:scale="{{duration: 200, opacity: 0.5, start: 1.1, easing: elasticInOut}}">
    <div class="side-panel__inner-container">
        <h1 class="side-panel__header">
            <span>Header</span> <Icon extraClass="icon--option square-4--important" faClass="fa-times" on:click={() => dispatch("sidePanelClose", null)} />
        </h1>
        <main>
            Hello
        </main>
    </div>
</aside>


<style>
.side-panel{
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    width: fit-content;
    z-index: 1000;
}
/* .side-panel::after{
    content: "";
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.5);
    z-index: 999;
} */
.side-panel__inner-container{
    width: 100%;
    height: 100%;
    background-color: white;
    position: relative;
    z-index: 1000;
    min-width: min(100vw, 400px);
    padding: 1.5rem;
    padding-top: calc(1.5rem + 5px);
}

.side-panel__header{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
/* .icon--option{
    height: 1rem;
    width: 1rem;
} */




</style>