<script>

export let type = "ellipsis";
export let extraClasses = "";
</script>



{#if type === "ellipsis"}
<div class={`lds-ellipsis ${extraClasses}`}><div></div><div></div><div></div><div></div></div>

<!-- {:else if type === ""} -->


{/if}



<style>
/** Ellipsis*/
.lds-ellipsis {
    display: inline-block;
    position: relative;
    --size: 80px;
    --movement: calc(var(--size, 80px) * .6 / 2);
    --gutter: calc(var(--size, 80px) * .4 / 2);
    width: 80px;
    height: 80px;
    width: var(--size, 80px);
    height: var(--size, 80px);
}
.lds-ellipsis div {
    position: absolute;
    --dot-size: calc(var(--size, 80px) * 0.1625);
    top: 33px;
    top: calc((var(--size, 80px) - var(--dot-size, 13px)) / 2);
    width: 13px;
    width: var(--dot-size);
    height: 13px;
    height: var(--dot-size);
    border-radius: 50%;
    background: #fff;
    background: rgb(204, 35, 35);
    animation-timing-function: cubic-bezier(0, 1, 1, 0);
    display: inline-block;
}
.lds-ellipsis div:nth-child(1) { left: 8px;  left: var(--gutter, 8px); animation: lds-ellipsis1 0.6s infinite; }
.lds-ellipsis div:nth-child(2) { left: 8px;  left: var(--gutter, 8px); animation: lds-ellipsis2 0.6s infinite; }
.lds-ellipsis div:nth-child(3) { left: 32px; left: calc(var(--gutter, 8px) + 1*var(--movement, 24px)); animation: lds-ellipsis2 0.6s infinite; }
.lds-ellipsis div:nth-child(4) { left: 56px; left: calc(var(--gutter, 8px) + 2*var(--movement, 24px)); animation: lds-ellipsis3 0.6s infinite; }
@keyframes lds-ellipsis1 { 0% { transform: scale(0);} 100% { transform: scale(1);} }
@keyframes lds-ellipsis3 { 0% { transform: scale(1);} 100% { transform: scale(0);} }
@keyframes lds-ellipsis2 { 0% { transform: translate(0, 0);} 100% { transform: translate(var(--movement, 24px), 0);} }

</style>