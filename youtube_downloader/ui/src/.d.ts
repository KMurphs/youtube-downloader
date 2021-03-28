declare namespace svelte.JSX {
    interface HTMLAttributes<T> {
        longpress?: (e: any) => void,
        onlongpress?: (e: any) => void, // necessary to prevent warning from compiler
    }
}
// This is only to support non standard events on DOM elements
// To type custom events on components, use: 
//   Create dispatcher 
//      const dispatchKeyDown = createEventDispatcher<{keydown: KeyboardEvent}>();
//   Use dispatcher inside inner element
//      on:keydown={e=>dispatchKeyDown("keydown", e)}
//   Handle dispatched event outside inner element
//      on:keydown={(e)=>handle(e.detail)}
// https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/typescript.md#typing-component-events