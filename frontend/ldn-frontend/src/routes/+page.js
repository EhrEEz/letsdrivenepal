const uri = 'http://127.0.0.1:8000/';
export async function load({ fetch }) {
	const res = await fetch(uri + 'api/precise/open-vehicles/');
	const data = await res.json();
	if (res.ok) {
		return { results: data };
	}
}
