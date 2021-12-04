## Await 블럭

대부분의 웹 어플리케이션은 특정 시점에서 비동기 데이터를 처리해야 합니다. Svelte를 사용하면 마크업에서 직접 Promise 상태에 따라 관리할 수 있습니다.

```svelte
{#await promise}
	<p>...waiting</p>
{:then number}
	<p>The number is {number}</p>
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
```

> 가장 최근의 Promise만 고려되므로 경쟁 조건에 대해 걱정할 필요가 없습니다.

Promise가 Reject되지 않는다는것을 알고 있다면 `catch` 구문을 생략 가능합니다.

또한 Promise가 Resolve될때까지 다른 컴포넌트를 표시하지 않고 싶다면 다음과 같이 작성 가능합니다.

```svelte
{#await promise then value}
	<p>the value is {value}</p>
{/await}
```
