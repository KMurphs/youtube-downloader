// https://svelte.dev/repl/f34b6159667247e6b6abb5142b276483?version=3.6.3
export function longpress(node, threshold = 500) {
    
	const handle_mousedown = () => {
		let start = Date.now();
		
		const timeout = setTimeout(() => {
            console.log("Here")
			node.dispatchEvent(new CustomEvent('longpress'));
		}, threshold);
		
		const cancel = () => {
			clearTimeout(timeout);
			node.removeEventListener('mousemove', cancel);
			node.removeEventListener('mouseup', cancel);
		};
		
		node.addEventListener('mousemove', cancel);
		node.addEventListener('mouseup', cancel);
	}
	
	node.addEventListener('mousedown', handle_mousedown);
	
	return {
		destroy() {
			node.removeEventListener('mousedown', handle_mousedown);
		}
	};
}