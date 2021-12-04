## Props

실제 응용 프로그램에서는 한 구성 요소에서 하위 구성 요소로 데이터를 전달해야 합니다.
그렇게 하려면 일반적으로 (react 하신분이라면 아시다시피) **'props'**이라는 속성을 선언해야 합니다.

Svelte에서는 export 키워드로 props을 선언합니다.

```svelte
<!-- down.svelte -->
<script>
	export let answer;
</script>
```

```svelte
<!-- up.svelte -->
<script>
	import Nested from './down.svelte';
</script>

<Nested answer={42}/>
```

### Default Props

props를 지정해주지 않았다면 default 값으로 설정됩니다.

```svelte
<!-- down.svelte -->
<script>
	export let answer = 123;
</script>
```

다음과 같이 선언해주면 됩니다.

### Spread Props

Props 개체가 있는 경우 각 속성을 지정하는 대신 Props에 rest로 적용시켜줄 수 있습니다.

```svelte
<script>
	import Info from './Info.svelte';

	const pkg = {
		name: 'svelte',
		version: 3,
		speed: 'blazing',
		website: 'https://svelte.dev'
	};
</script>

<Info name={pkg.name} version={pkg.version} speed={pkg.speed} website={pkg.website}/>
```

into

```svelte
<script>
	import Info from './Info.svelte';

	const pkg = {
		name: 'svelte',
		version: 3,
		speed: 'blazing',
		website: 'https://svelte.dev'
	};
</script>

<Info {...pkg}/>
```
