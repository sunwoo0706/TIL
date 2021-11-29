## Svelte 스타일링

간단합니다 .svelte 컴포넌트 안에 style 태그를 선언하고 그 안에 css를 작성하면 됩니다.

```html
<p>This is a paragraph.</p>

<style>
  p {
    color: purple;
    font-family: "Comic Sans MS", cursive;
    font-size: 2em;
  }
</style>
```

이 챕터에서 알아갈 중요한 것은 저렇게 선언된 css는 전역적이 아닌 컴포넌트 스코프 범위에서만 할당합니다.
css_module 같은걸 써서 css 식별을 따로 하지 않아도 된다는겁니다.
