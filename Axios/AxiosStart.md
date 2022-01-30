## 시작하기

axios는 node.js와 브라우저를 위한 Promise 기반 HTTP 클라이언트이다. axios는 동형이라고 공식 문서에서 소개하고 있다. 여기서 동형 (isomrphic application) 이란, 한마디로 서버와 클라이언트 모두에서 실행할 수 있는 응용 프로그램을 말한다.
서버에서 사용할 때는 `http` 모듈을 사용하고, 클라이언트에서는 `XMLHttpRequests` 를 사용한다.

### Axios의 특징

- 브라우저를 위해 XHR 생성
- node.js를 위해 http 요청 생성
- Promist API를 지원
- 요청 및 응답 인터셉트
- 요청 및 응답 데이터 변환
- 요청 취소
- JSON 데이터 자동 변환
- XSRF를 막기위한 클라이언트 사이드 지원

### 설치 방법

npm

```sh
$ npm install axios
```

bower

```sh
$ bower install axios
```

yarn

```sh
$ yarn add axios
```

jsDelivr

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

unpkg CDN 사용하기

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```
