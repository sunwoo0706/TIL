## 반응성

Svelte의 가장 중요한 기능중 하나는 DOM을 App 상태와 동기화 상태로 유지하기 위한 강력한 반응성 시스템입니다.

```svelte
<script>
	let count = 0;

	function incrementCount() {
		count += 1;
	}
</script>

<button on:click={incrementCount}>
	Clicked {count} {count === 1 ? 'time' : 'times'}
</button>
```

svelte는 위 코드를 보고 count가 변할때마다 dom에 sync해줘야 한다는 것을 계측합니다.

### 반응성 선언

종종 구성 요소 상태의 일부는 다른 부분에서 계산되어야 하고 변경될 때마다 다시 계산해야 합니다.
(예 : `fullname`은 `lastname`이나 `firstname`이 변경되면 같이 변경되어야 겠지요?)

이 경우를 위해 svelte는 반응성 선언 (Reactivity Declation)이 있습니다. 다음과 같이 사용합니다.

```svelte
let firstname = lee;
let lastname = sunwoo;
$: fullname = firstname + lastname;
```

`$:` 이는 바닐라 자바스크립트의 `label`을 이용한 기능입니다. svelte는 이 구문에 특별한 의미를 부여하여 반응성을 자동으로 계측합니다.
