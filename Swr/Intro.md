## SWR

SWR의 이름의 유래는 [HTTP RFC 5861](https://tools.ietf.org/html/rfc5861)에 의해 알려진 HTTP 캐시 무효 전략인 `stale-while-revalidate` 에서 유래되었다.
SWR은 먼저 캐시로부터 데이터를 반환한 후, fetch 요청을 하고, 최종적으로 최신화된 데이터를 가져오는 전략이다.

### 개요

```js
import useSWR from "swr";

function Profile() {
  const { data, error } = useSWR("/api/user", fetcher);

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;
  return <div>hello {data.name}!</div>;
}
```

위의 예시를 보면 `useSwr` hook은 `key` 문자열과 `fetcher` 함수를 인자로 받는다. `key` 는 데이터의 고유한 식별자이며(일반적으로 API URI) `fetcher` 로 전달된다. `fetcher`는 데이터를 반환하는 비동기 함수라면 무엇이든지 된다. 네이티브 fetch 또는 axios와 같은 라이브러리를 사용해도 된다.

hook은 요청의 상태에 기반한 `data`와 `error` 두 개의 값을 반환한다.

위와 같이 단 한 줄의 코드로 프로젝트 내의 데이터 가져오기 로직을 단순화할 수 있으며, 다음과 같은 모든 놀라운 기능들을 사용할 수 있다.

### 설치

React 프로젝트 폴더 안에서 다음을 실행하여 SWR을 설치한다.

```sh
yarn add swr
```

### 빠른 대전

REST API라면 axios나 fetch를 이용하여 fetcher를 생성해야 한다.

```js
const fetcher = (...args) => fetch(...args).then((res) => res.json());
```

그 다음, `useSWR`을 사용하여 시작하면 된다.

```js
import useSWR from "swr";

function Profile() {
  const { data, error } = useSWR("/api/user/123", fetcher);

  if (error) return <div>failed to load</div>;
  if (!data) return <div>loading...</div>;

  // 데이터 렌더링
  return <div>hello {data.name}!</div>;
}
```

일반적으로, 세 가지 요청 상태가 있다. "loading", "ready", "error". data와 error 값을 사용해 현재 요청의 상태를 알아내고, 해당하는 UI를 반환할 수 있다.

### 재사용

컴포넌트 기반의 웹 앱을 구축할 때, UI의 많은 곳에서 데이터를 재사용할 필요가 있을 것이다. 그럴때는 swr을 이용하여 커스텀 훅을 만들어 쓰면 아주 쉽다.

```js
function useUser(id) {
  const { data, error } = useSWR(`/api/user/${id}`, fetcher);

  return {
    user: data,
    isLoading: !error && !data,
    isError: error,
  };
}
```

그리고 컴포넌트에서 다음과 같이 사용하면 된다.

```js
function Avatar({ id }) {
  const { user, isLoading, isError } = useUser(id);

  if (isLoading) return <Spinner />;
  if (isError) return <Error />;
  return <img src={user.avatar} />;
}
```
