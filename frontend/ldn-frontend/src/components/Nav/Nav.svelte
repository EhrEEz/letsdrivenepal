<script>
	import './style.scss';

	// import { IconBellFilled } from '@tabler/icons-svelte';
	export let currentPage = '';
</script>

<nav class="nav__main">
	{#if currentPage !== 'login' && currentPage !== 'register'}
		<div class="nav__breadcrumbs--wrapper">
			<ul class="nav__breadcrumbs--list">
				<li class="nav__breadcrumbs--item">
					<a href="#" class="nav__breadcrumbs--link">Home</a>
				</li>
				<li class="nav__breadcrumbs--item">
					<a href="#" class="nav__breadcrumbs--link">Your Vehicles</a>
				</li>
				<li class="nav__breadcrumbs--item">
					<a href="#" class="nav__breadcrumbs--link">Hyundai I20</a>
				</li>
			</ul>
		</div>
		<div class="nav__user--wrapper">
			<div class="nav__user--notifications">
				<button class="round--btn notification">
					<!-- <IconBellFilled /> -->'B'
				</button>
			</div>
			<div class="nav__user--disp">
				<div class="nav__user--avatar">
					<img src="assets/user-icon.png" alt="User Icon" />
				</div>
				<div class="nav__user--title">John Doe</div>
				<div class="nav__user--indicator">|</div>
			</div>
		</div>
	{/if}
</nav>
