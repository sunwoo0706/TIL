## Each 블럭

데이터 리스트를 야물딱지게 프로그래머처럼 반복해야 하는 경우 `each`블럭을 쓰면 됩니다.

```svelte
<ul>
	{#each cats as cat}
		<li><a target="_blank" href="https://www.youtube.com/watch?v={cat.id}">
			{cat.name}
		</a></li>
	{/each}
</ul>
```

> 배열 객체를 이용하고 싶다면 다음과 같이 표시할 수 있습니다.
> `each [...iterable]`

다음과 같이 현재 인덱스를 두 번째 인수로 가져올 수 있습니다.

```svelte
{#each cats as cat, i}
	<li><a target="_blank" href="https://www.youtube.com/watch?v={cat.id}">
		{i + 1}: {cat.name}
	</a></li>
{/each}
```

비구조화 할당해서 사용할 수 있습니다. `{ id, name }`, `cat.id => id`, `cat.name => name`

### keyed each blocks

기본적으로 `each` 블럭의 내부 값에 변화가 생긴다면 블럭의 마지막부터 변화에 의해서 수정됩니다. 당연히 원하는 결과가 아니겠죠? 이럴때는 key를 쓰면 됩니다.

```svelte
{#each cats as cat {cat.id}}
	<div name={cat.name}>
{/each}
```

여기서 (thing.id)는 구성 요소가 업데이트될 때 변경할 DOM 노드를 파악하는 방법을 Svelte에 알려주는 역할을 하는 키가 되는거죠.
