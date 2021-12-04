## 데이터 추가하기

svelte 컴포넌트에 데이터를 추가하고 싶으면 간단하게 다음과 같이 추가가능하다.

```html
<script>
  let name = "이선우";
</script>

<h1>{name}</h1>
```

다음과 같이 script 태그 내에서 변수를 선언하고, html 태그에 삽입하면 됩니다.

{} 템플릿 안에서 Js 연산도 가능합니다.

```html
<script>
  let name = "이선우";
</script>

<h1>{name + "최고"}</h1>
```
