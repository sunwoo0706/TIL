## svelte 라이프 사이클

모든 svelte 컴포넌트는 생명주기를 가지고 있습니다.

### 라이프 사이클 모듈화

Svelte의 라이프 사이클 함수는 어디서 사용할지는 중요하지 않습니다.

```js
// utils.js
import { onDestroy } from "svelte";

export function onInterval(callback, milliseconds) {
  const interval = setInterval(callback, milliseconds);

  onDestroy(() => {
    clearInterval(interval);
  });
}
```

```js
<script>
  import { onInterval } from './utils.js';

  let seconds = 0;
  onInterval(() => seconds += 1, 1000);
</script>

<p>
  The page has been open for
  {seconds} {seconds === 1 ? 'second' : 'seconds'}
</p>
```

---

> `서버 사이드 랜더링(Server Side Rendering)` 중에는, `onDestroy` 라이프 사이클 함수를 제외한 다른 라이프 사이클 함수들은 실행되지 않습니다. 서버 사이드 랜더링되는 동안에 onMount 라이프 사이클 함수가 실행되지 않기 때문에, 마운트 된 후에 실행되는 onMount에서 데이터를 가져오면, 데이터를 가져오느라 DOM이 느리게 마운트 되는 문제를 피할 수 있습니다.

### onMount

가장 많이 사용되는 라이트 사이클 함수입니다. 이 함수는 컴포넌트가 처음으로 DOM에 렌더링 될 때 실행되는 함수입니다.

네트워크를 통해 데이터를 가져와 느리게 데이터가 세팅이 된다면, `<script>` 태그의 상단이 아닌 `onMount` 라이프 사이클 함수에서 가져오는 것이 좋습니다.

### onDestroy

`onDestroy`는 컴포넌트가 제거되었을 때 호출됩니다. 컴포넌트가 할당받은 자원을 해제할 때 사용되는 라이프 사이클 함수입니다.

---

예시

위의 코드와 같이 Svelte는 라이프 사이클 함수를 다른 파일에 작성하고 컴포넌트에 `import`하여 사용할 수 있기 때문에, 기능별로 모듈화하기 쉽습니다.

### beforeUpdate

`beforeUpdate`는 DOM이 업데이트되기 직전에 호출되는 라이프 사이클 함수입니다.

`beforeUpdate` 라이프 사이클 함수는 마운트 되기 전에도 호출되기 때문에 DOM에 접근할 때 DOM이 존재하는지 체크하는 로직이 필요합니다.

### afterUpdate

`afterUpdate`는 DOM이 업데이트된 직후에 호출되는 라이프 사이클 함수입니다.

---

### tick

`tick`은 다른 라이프 사이클 함수들과 다르게 언제든 사용할 수 있습니다. 언제든 사용할 수 있다는 뜻은 마운트 된 후에만 호출되는 `onMount`, 제거된 후에만 호출되는 `onDestroy` 와는 달리 언제든 호출된다는 뜻입니다. `tick`함수는 변경된 내용이 있다면 변경된 내용이 DOM에 반영된 직후에, 변경된 내용이 없다면 바로 호출됩니다.
