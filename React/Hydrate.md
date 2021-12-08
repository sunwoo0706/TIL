## Hydrate

React는 JS만을 이용하여 웹 화면을 구성하는 원리를 가지고 있다. 그래서 CRA로 생성한뒤 `public/` 디렉토리 하위의 HTML코드는 `<div id="root"></div>` 말고는 body 태그안에 아무런 내용이 없다.

```html
// public/index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

위 코드처럼 `public/index.html`에는 아무 내용 없는 기본 뼈대만 있고, 나머지는 `src/index.js`의 자바스크립트 코드에서 모든 화면을 렌더링 한 뒤 `HTML DOM` 요소 중 `root`라는 아이디를 가진 엘리먼트를 찾아서 하위로 주입을 하게 된다.

react-snap이나 Next.js를 사용하면 클라이언트에게 웹 페이지를 보내기 전에 미리 웹 페이지를 `pre-rendering` 한다. 그리고 `pre-rendering` 으로 인해 생성된 HTML document를 클라이언트에게 전송한다.

그런데 여기서 중요한 것은 현재 클라이언트가 받은 웹 페이지는 단순히 웹 화면만 보여주는 HTML뿐이고, 자바스크립트 요소들이 하나도 없는 상태이다. 이는 웹 화면을 보여주고 있지만, 이벤트들이 하나도 작동이 되지 않는 상태임을 말한다.

그러면 이렇게 페이지만 보여주고 동작조차 하지 못하는 마치 빈 껍데기 같은 웹 페이지가 나중에는 어떻게 정상적으로 동작하게 되는 것일까?

예를 들어서 설명하자면 Next.js Server에서는 사전 렌더링된 웹 페이지를 클라이언트에게 보내고 나서, 바로 리액트가 번들링 된 자바스크립트 코드들을 클라이언트에게 전송한다.

![콴다예시](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIKpSq%2FbtrbvxzOgG8%2FdUjyHq88JuZSKEE8FVdqdK%2Fimg.png)

콴다는 Next를 쓴답니다. 네트워크 탭을 보면, 맨 처음 응답받는 요소가 dom type의 파일이고, 이후에 React 코드들이 렌더링 된 JS 파일들이 Chunk 단위로 다운로드되는 것을 확인할 수 있다.

그리고 이 자바스크립트 코드들이 이전에 보내진 HTML DOM 요소 위에서 한번 더 렌더링을 하면서, 각자 자기 자리를 찾아가며 매칭이된다.

바로 이 과정을 **Hydrate** 라고 한다.

이것은 마치 자바스크립트 코드들이 DOM 요소 위에 물을 채우 듯 필요로 하던 요소들을 채운다 하여 Hydrate(수화)라는 용어를 쓴다고 한다.

![수화예시](https://mblogthumb-phinf.pstatic.net/20160622_53/sp_ht_14666074103672hWKQ_JPEG/%C1%D6%C1%B61.jpg?type=w800)

> 물은 아니지만 이런 느낌이랄까..

어쩌면 두번 렌더링 하는 것은 비효율적으로 보일 수 있다.

그러나 서버 단에서 빠르게 Pre-Rendering하고 유저에게 빠른 웹 페이지로 응답할 수 있다는 것에 더욱 큰 이점을 가져갈 수 있다.

심지어 이 Pre-Rendering 한 Document는 모든 자바스크립트 요소들이 빠진 굉장히 가벼운 상태이므로 클라이언트에게 빠른 로딩이 가능하다.

이는 같은 화면에 대해 두 번 렌더링이 일어난다는 단점을 보완하고도 남는다.
