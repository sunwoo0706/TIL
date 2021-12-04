## 컴포넌트 중첩

여러분들도 아시다시피 하나의 요소에 모든 하위요소를 때려박으면 유지보수하기도 힘들고 개발할때 당시도 힘들게 됩니다.

`default import`로 컴포넌트를 `<script>` 태그에서 받아온후에 HTML 부분에 작성해주면 됩니다.

```html
<script>
  import Nested from "./Nested.svelte";
</script>
```

```html
<p>This is a paragraph.</p>
<Nested />
```

또한 component는 대문자로 작성되어야 합니다.

이 규칙은 리액트와 같이 DOM태그와 사용자 지정 컴포넌트가 구분되기 위해 정해진 규칙입니다.
