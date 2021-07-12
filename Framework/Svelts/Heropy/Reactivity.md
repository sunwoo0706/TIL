## 반응성

반응성은 변경된 값이 Dom에 자동으로 반영됨을 의미합니다.
Svelte는 별도의 Setter 없이 값의 할당만으로 업데이트를 트리거할 수 있습니다.
실제로 상당히 편리하다고 하네요

```html
<script>
  let count = 0;
</script>

<button on:click={() => count += 1}>
  {count}
</button>
```

컴파일 결과가 할당을 계측하고 DOM을 갱신합니다.

```js
// JS output

$$invalidate("count", (count += 1));
```
