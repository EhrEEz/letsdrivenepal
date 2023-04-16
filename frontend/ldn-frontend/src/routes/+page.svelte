<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

{#each data.results as vehicle (vehicle.id)}
	<div class="vehicle__card--wrapper" data-key={vehicle.id}>
		<div class="vehicle__card--title">
			{vehicle.model_manufacturer}
			{vehicle.model_name}
		</div>
	</div>
{/each}
