<script lang="ts">
	import { createEventDispatcher, onMount } from "svelte";
	const dispatch = createEventDispatcher();
	export let isOpen: boolean = false;
	import Icon from "./Icon.svelte";
	// import positionMenuItem from "./circular.menu.helpers";
	// onMount(()=>setTimeout(positionMenuItem, 1000));
</script>

<!-- <nav class="app-nav">
	<ul class="reset">
		<li><Icon faClass="fa-columns" on:click={() => dispatch("sidePanelOpen", null)}/></li>
		<li><Icon faClass="fa-info"/></li>
		<li><Icon faClass="fa-bars"/></li>
		<li><Icon faClass="fa-plus"/></li>
		<li><Icon faClass="fa-home"/></li>
	</ul>
</nav> -->

<nav class="app-nav nav nav--circular">
	<input type="checkbox" id="hamburger-menu-control" bind:checked={isOpen}>
	<label class="hamburger-menu" for="hamburger-menu-control">
		<span></span>
		<span></span>
		<span></span>
		<span></span>
	</label>
	<ul class="nav__items reset" on:click={()=>(isOpen = false)}>
		<li class="nav__item" style="--nth:1; --to-x:-126.504px; --to-y:1.54923e-14px;" on:click>
			<Icon extraClass="icon--btn m-0--important" faClass="fa-columns" on:click={() => dispatch("sidePanelOpen", null)}/>
		</li>
		<li class="nav__item" style="--nth:2; --to-x:-109.556px; --to-y:-63.252px;" on:click>
			<Icon extraClass="icon--btn m-0--important" faClass="fa-info"/>
		</li>
		<li class="nav__item" style="--nth:3; --to-x:-63.252px; --to-y:-109.556px;" on:click>
			<Icon extraClass="icon--btn m-0--important" faClass="fa-bars"/>
		</li>
		<li class="nav__item" style="--nth:4; --to-x:-2.32384e-14px; --to-y:-126.504px;" on:click>
			<Icon extraClass="icon--btn m-0--important" faClass="fa-plus"/>
		</li>
	</ul>
</nav>

<style>
.app-nav{
	position: absolute;
	right: 2rem;
	bottom: 2rem;
}













#hamburger-menu-control{
	display: none;
}
.hamburger-menu{
	width: 50px;
	height: 45px;
}
.hamburger-menu,
.nav__item{
	/* width: 50px; */
	/* height: 45px; */
	position: fixed;
	/* margin: 50px auto; */
	right: 2rem;
	/* top: 50%; */
	bottom: 2rem;
	display: inline-block;
	-webkit-transform: rotate(0deg) scale(.5);
	-moz-transform: rotate(0deg) scale(.5);
	-o-transform: rotate(0deg) scale(.5);
	transform: rotate(0deg) scale(.5);
	-webkit-transition: .5s ease-in-out;
	/* -webkit-transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275); */
	-moz-transition: .5s ease-in-out;
	/* -moz-transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275); */
	-o-transition: .5s ease-in-out;
	/* -o-transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275); */
	transition: .5s ease-in-out;
	/* transition: transform .3s cubic-bezier(0.175, 0.885, 0.32, 1.275); */
	cursor: pointer;
	z-index: 2000;
}
.hamburger-menu::before{
/* .nav__item::before{ */
	position: absolute;
	border-radius: 50%;
	background-color: rgba(0,0,0,0.05);
	background-color: #efefef;
	width: 100px;
	height: 100px;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	content: "";
	-webkit-transition: .25s ease-in-out;
	-moz-transition: .25s ease-in-out;
	-o-transition: .25s ease-in-out;
	transition: .25s ease-in-out;
	box-shadow: 0px 2px 4px 0 rgba(0, 0, 0, 0.14);
}
.hamburger-menu span {
	display: block;
	position: absolute;
	height: 9px;
	width: 100%;
	background: #d3531a;
	border-radius: 9px;
	opacity: 1;
	left: 0;
	-webkit-transform: rotate(0deg) scalex(1);
	-moz-transform: rotate(0deg) scalex(1);
	-o-transform: rotate(0deg) scalex(1);
	transform: rotate(0deg) scalex(1);
	-webkit-transition: .25s ease-in-out;
	-moz-transition: .25s ease-in-out;
	-o-transition: .25s ease-in-out;
	transition: .25s ease-in-out;
}

.hamburger-menu span:nth-child(1) {
	top: 0px;
}

.hamburger-menu span:nth-child(2),
.hamburger-menu span:nth-child(3) {
	top: 18px;
}

.hamburger-menu span:nth-child(4) {
	top: 36px;
}

#hamburger-menu-control:checked ~ .hamburger-menu span:nth-child(1) {
	top: 18px;
	width: 0%;
	left: 50%;
}
#hamburger-menu-control:checked ~ .hamburger-menu span:nth-child(2) {
	-webkit-transform: rotate(45deg) scale(.8);
	-moz-transform: rotate(45deg) scale(.8);
	-o-transform: rotate(45deg) scale(.8);
	transform: rotate(45deg) scale(.8);
}
#hamburger-menu-control:checked ~ .hamburger-menu span:nth-child(3) {
	-webkit-transform: rotate(-45deg) scale(.8);
	-moz-transform: rotate(-45deg) scale(.8);
	-o-transform: rotate(-45deg) scale(.8);
	transform: rotate(-45deg) scale(.8);
}
#hamburger-menu-control:checked ~ .hamburger-menu span:nth-child(4) {
	top: 18px;
	width: 0%;
	left: 50%;
}
#hamburger-menu-control:checked ~ .hamburger-menu::before {
	width: 80px;
	height: 80px;
}
.nav__item:hover::before,
.hamburger-menu:hover::before {
	background-color: rgba(0,0,0,0.08);
	background-color: #ddd;
}
.hamburger-menu:hover span {
	-webkit-transform: scaleX(1.05);
	transform: scaleX(1.05); 
}
.hamburger-menu:hover {
	-webkit-transform: scale(.55);
	transform: scale(.55); 
}





.nav__item{
	display: flex;
	justify-content: center;
	align-items: center;
	opacity: 0;
	z-index: 1999;
	transition: opacity ease-out 200ms, transform ease-out 200ms, -webkit-transform ease-out 200ms;
	-webkit-transition-timing-function: cubic-bezier(0.935, 0, 0.34, 1.33);
	transition-timing-function: cubic-bezier(0.935, 0, 0.34, 1.33);
	transition-duration: 180ms;
	-webkit-transition-duration: 180ms;
	-webkit-transform: translate3d(0px, 0px, 0px);
	transform: translate3d(0px, 0px, 0px);
	counter-increment: item-position;
}
.nav__item::before{
	width: 60px;
	height: 60px;
}












/* #hamburger-menu-control:checked ~ .nav__items > .nav__item:nth-child(1) { */
#hamburger-menu-control:checked ~ .nav__items > .nav__item {
	opacity: 1;
	transition-duration: 180ms;
	-webkit-transition-duration: 180ms;
	transition-duration: calc(var(--nth) * 100ms + 180ms);
	-webkit-transition-duration: calc(var(--nth) * 100ms + 180ms);
	-webkit-transform: translate3d(0.08361px, -104.99997px, 0);
	transform: translate3d(0.08361px, -104.99997px, 0);
	-webkit-transform: translate3d(var(--to-x), var(--to-y), 0);
	transform: translate3d(var(--to-x), var(--to-y), 0);
}

</style>