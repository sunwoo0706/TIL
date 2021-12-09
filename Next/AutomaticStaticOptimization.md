## Automatic Static Optimization

`Next.js`는 블로킹 데이터 요청 (예를 들면 API 요청)의 여부로 페이지를 사전 렌더링할지 정하게 된다.
이 결정은 페이지에 `getServerSideProps` 및 `getInitialProps`의 여부에 따라 달라진다.

static page도 일반 페이지들과 마찬가지로 우저와 상호작용 할 수 있다. (가령 클릭 이벤트 같은것) Next가 알아서 [Hydrate](../React/Hydrate,md) 과정을 진행해 주기 때문이다.

이 `Automatic Static Optimization`의 주요 이점 중 하나는 최적화된 페이지에는 서버 사이드 연산이 필요하지 않고, 여러 CDN에서 사용자에게 즉시 HTML로 사전 렌더링된 페이지를 보내줄 수 있다. (이미 사전 렌더링이 되어 있기에)

결과적으로 사용자에게 하이퍼 울트라 빠른 웹페이지 로딩 속도를 경험하게 할 수 있다.

### 어떻게 작동하나요?

만약 `getServerSideProps`나 `getInitialProps`가 페이지에 있다면, Next.js는 렌더링 방식을 사전 렌더링이 아닌 서버 사이드 렌더링을 시킨다.

위의 경우가 아니라면 Next.js는 페이지를 정적 HTML로 미리 렌더링하여 **자동**으로 페이지를 **정적**으로 **최적화**한다.

사전 렌더링 동안 라우터의 query객체는 제공할 쿼리 정보가 없기 때문에 비어 있습니다. hydration후 Next.js는 query객체에 router parameter를 제공하기 위해 당신의 앱을 업데이트를 트리거한다.

> getStaticProps를 사용하는 페이지에 동적 경로와 함께 추가된 매개변수는 쿼리 객체 내에서 언제든지 사용할 수 있다.

`next build` 는 정적으로 최적화된 페이지에서는 HTML 파일을 방출한다.

예를 들어 `getServerSideProps` 및 `getInitialProps` 가 없는 `pages/about.js`는 다음과 같이 변환된다.

```sh
.next/server/pages/about.html
```

그리고 만약 `getServerSideProps` 및 `getInitialProps`이 있다면 다음과 같이 JS파일이 된다.

```sh
.next/server/pages/about.js
```

### 주의 사항

만약에 `getInitialProps`가 있는 커스터마이징 APP 컴포넌트가 있는 경우 정적 생성이 없는 페이지에서는 이 최적화가 기능하지 않는다.

`getInitialProps`가 있는 커스터마이징 DOCUMENT 컴포넌트가 있는 경우 페이지가 서버 사이드 렌더링됐다고 가정하기전에 `ctx.req`가 있는지 확인해야한다. `ctx.req`는 사전 렌더링된 페이지에서는 `undefined`가 된다.
