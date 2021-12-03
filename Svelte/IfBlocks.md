## 조건 블럭

HTML은 프로그래밍 로직을 포함할 수 없다는 건 알고 계실겁니다.

일부 마크업을 조건부로 렌더링하기 위해 if블록으로 래핑해주면됩니다.

```svelte
{#if user.loggedIn}
	<button on:click={toggle}>
		Log out
	</button>
{/if}

{#if !user.loggedIn}
	<button on:click={toggle}>
		Log in
	</button>
{/if}
```

### Else 블럭

`user.loggedIn`과 `!user.loggedIn`의 두 조건은 상호 배타적이므로 `else` 블록을 사용하여 이 구성 요소를 약간 단순화할 수 있습니다

```svelte
{#if user.loggedIn}
	<button on:click={toggle}>
		Log out
	</button>
{:else}
	<button on:click={toggle}>
		Log in
	</button>
{/if}
```

### Else if 블럭

```svelte
{#if x > 10}
	<p>{x} is greater than 10</p>
{:else if 5 > x}
	<p>{x} is less than 5</p>
{:else}
	<p>{x} is between 5 and 10</p>
{/if}
```

`{:else 조건문}` 처럼 작성하면 됩니다.

---

> `#` 문자는 항상 블록 열기 태그를 나타냅니다. `/` 문자는 항상 블록 닫기 태그를 나타냅니다. `:` 문자는 {:else}에서와 같이 블록 연속 태그를 나타냅니다.
