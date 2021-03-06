declare namespace svelte.JSX {
    interface HTMLAttributes<T> {
        longpress?: (e: any) => void,
        onlongpress?: (e: any) => void, // necessary to prevent warning from compiler
    }
}