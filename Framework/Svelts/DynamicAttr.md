## 동적 속성

중괄호를 사용하여 문자열을 제어할 수 있는 것처럼 중괄호를 사용하여 요소 속성을 제어할 수 있습니다.

```svelte
<img src={src}>
```

> `<img>` 요소에는 alt 속성이 있어야 합니다.

```svelte
<img src={src} alt="A man dances.">
```

속성 내에서 중괄호를 사용할 수 있습니다.

### Shorthand attributes

`Svelte`는 다음과 같이 src={src}의 경우에는 다음과 같은 편리한 약칭을 제공합니다.

```svelte
<img {src} alt="A man dances.">
```
