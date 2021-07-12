## Svelte 시작하기

> Svelte는 런타임 프레임워크가 아니기 때문에, CDN을 제공하지 않습니다!

### svelte/template

Degit을 이용해 Rollup.js 기반의 새로운 프로젝트를 생성합니다.
[공식 레포](https://github.com/sveltejs/template)에서 템플릿 구조를 확인할 수 있습니다.

svelte에서 공식적으로 지원해주는 템플릿은 총 두개가 있다

- https://github.com/sveltejs/template
  Rollup을 사용

- https://github.com/sveltejs/template-webpack
  webpack을 사용

> Rollup 중심적인 생태계가 생성중이니 되도록이면 기본 템플릿을 사용하시는것을 추천합니다.

```sh
npx degit sveltejs/template svelte-template-test
```

`degit`은 깃헙 레포지터리를 아주 잘 클론시켜주는 패키지
