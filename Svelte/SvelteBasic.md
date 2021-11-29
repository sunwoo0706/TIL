## Svelte 기본

> 본인은 svelte의 가능성을 보고 남들보다 미리 공부를 시작했다.
> ps. svelte 만은 Rich Haris가 vercel 들어갔다. 이 정도면 굉장히 유망있다고 본다.

svelte는 빠른 웹사이트를 구축하기 위한 도구입니다.
React와 Vue와 같은 프레임워크와 흡사합니다. (이제 Angular는 비교축에도 들지 않네요..)

Svelte는 런타임에 애플리케이션 코드를 해석하지 않고 빌드 시 앱을 이상적인 JavaScript로 변환합니다

Svelte에서 애플리케이션은 하나 이상의 구성 요소로 구성됩니다.
구성 요소는 .svelte 파일로 작성된 HTML, CSS 및 JavaScript를 캡슐화하는 재사용 가능한 자체 포함 코드 블록입니다.

```html
<script>
  let name = "이선우";
</script>

<h1>{name}</h1>

<style>
  h1 {
    color: red;
  }
</style>
```

다음과 같이 컴포넌트가 이루어져있죠
