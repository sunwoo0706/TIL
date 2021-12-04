## 동적 HTML 속성

data 추가하기 처럼 `HTML Attr` 삽입해줄 수 있습니다.

```svelte
<img src={src} />
```

하지만 이렇게 작성한다면 `svelte`는 우리에게 warning 메세지를 출력할것입니다.

```sh
A11y: <img> element should have an alt attribute
```

이건 웹 접근성과 관련이 되어있는데요. 인터넷이 느리거나 시각장애인들은 사진 정보를 받지 못하게 될 수 있습니다. 이를 위해 `HTML`에는 `alt` 속성이 있는데요. 이를 추가해주어야 합니다.

이에 더해 `svelte`에서는 `alt`와 같은 속성에 동적으로 데이터를 삽입할 수 있는데요.

```svelte
<script>
    let alt = "남자가 웃고 있는 사진";
</script>

<img src={src} alt="멋진 {alt}" />
```

이런식으로 작성할 수 있습니다.

### 단축 attr

이것은 TIP인데 attr의 이름과 변수명이 같다면 다음과 같이 축약해서 사용가능합니다.

```svelte
    <img {src} alt="A man dances.">
```
