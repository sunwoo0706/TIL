## 외부 종속 라이브러리

> svelte는 CDN이 안됩니다.

### TypeScript

타입스크립트를 사용하는 경우 다음과 같이 작성할 수 있습니다.

```svelte
<script lang="ts">let count: number = 0</script>
```

### Sass

SCSS를 사용하는 경우 다음과 같이 작성할 수 있습니다.

```svelte
<style lang="scss">
  $color--primary: royalblue;
  h1 {
    color: $color--primary;
  }
</style>
```
