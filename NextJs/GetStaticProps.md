## getStaticProps

`getStaticProps` 라고 불리는 async function가 page에서 export되면, Next.js는 `getStaticProps`가 반환한 `props` 를 사용하여 해당 page를 사전렌더링 하게 된다.

```js
// getStaticProps 예시 코드
export async function getStaticProps(context) {
  return {
    props: {}, // will be passed to the page component as props
  }
}
```

---

### context

`getStaticProps`가 파라미터로 가져오는 `context`는 객체이고 다음 `key` 들을 갖고 있다.

- `params` 는 동적 라우팅을 사용한 page일 경우 route parameter들을 가지고 있다. 예를 들어 page의 이름은 `[id].js` 일 경우, `params` 는 다음과 같은 객체가 될 것이다.
`
{
    id: ...
}
`
그리고 `params` 를 쓰고 싶다면 `getStaticPaths` 를 함께 사용해야 한다.

- `preview` 는 해당 page가 `preview mode` 일 경우에는 `true` 이고, 그렇지 않은 경우에는 `undefined`가 된다.

- `previewData` 는 `setPreviewData` 로 인해 설정된 `preview data set`을 갖고 있다.

- `locale` 은 활성 locale을 가지고 있다.

- `locales` 는 활성이든 비활성이든 모든 지원되는 locale을 가지고 있다.

- `defaultLocale` 은 `locale` 의 기본값을 가지고 있다.

---

### getStaticProps가 반드시 반환해야 하는 객체의 key들

- `props` 는 optional 객체로 page 컴포넌트에 전달될 `props` 를 가지고 있다. 직렬화가 가능한 객체여야 한다.

- `revalidate` 는 optional revalidate(페이지 정적 재생성 발생 시간을 정의한 시간 초)의 초 값이다. 기본값은 `false` 이다.

- `notfound` 는 optional 불린값으로 page가 404 상태 및 404 page를 반환하도록 허용한다. 아래 예시를 보자

```js
export async function getStaticProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

> `notFound` 는 `getStaticPaths` 에서 반환된 경로만 사전 렌더링 되므로 `fallback: false` 가 필요하지 않다.

> `notFound: true` 를 사용하면 이전에 성공적으로 생성된 페이지가 있더라도 페이지가 404를 반환한다. 이는 블로그와 같이 사용자가 생성 콘텐츠와 같은 사용 사례를 지원하기 위한 것이다.

- `redirect` 는 optional redirect value이다. 외부나 내부 자원으로 redirect 될 수 있도록 허락해준다. 다음과 같은 형식이어야 하며 `{
    destination: string,
    permanent: boolean
}`, 아주 희귀한 경우 오래된 HTTP Clients에 제대로 redirect 하기 위해서는 사용자 지정 HTTP 상태 코드를 할당해야 할 수도 있다. 이 경우에는 당신은 `permanent` 속성 대신에 `statusCode` 속성을 사용할 수 있다. (둘다 사용 불가능)
`next.config.json`의 redirect와 유사하게 `basePath: false`를 설정할 수도 있다. 아래 코드는 예시이다.

```js
export async function getStaticProps(context) {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!data) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
      },
    }
  }

  return {
    props: { data }, // page 컴포넌트에 props로 전달될 것 이다.
  }
}
```

> 빌드타임에 리다이렉팅은 현재 허용되지 않는다. 리다이렉팅이 빌드타임에 리다이렉팅들은 `next.config.json` 에 추가하여야 한다.

> `getStaticProps` 에서 사용하기 위한 모듈을 최상위에서 import 할 수 있다. getStaticProps에서 사용된 import 로 가져온 모듈들은 클라이언트 측에서 번들링 되지 않는다. 즉 `getStaticProps` 에서 직접 서버 사이드 코드를 작성할 수 있다. 여기에는 파일 시스템 읽기나 데이터베이스 정보 가져오기가 포함된다.

> `getStaticProps` 안에서 fetch를 사용하여 API route를 호출하며 안 된다. 대신 API 경로 내에서 사용되는 로직을 작성해야한다. 외부 API에서 가져오는 것은 상관없다.

### getStaticProps 사용 예시

```js
// posts will be populated at build time by getStaticProps()
function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries. See the "Technical details" section.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}

export default Blog
```

### 언제 쓰나요?

- 사용자 요청에 앞서서 build 시에 페이지를 사전 렌더링하여 이용할 데이터가 있을때
- headeless CMS로부터 오는 데이터가 있다면
- 개개인이 아닌 모두에게 공개적으로 캐시될 수 있는 데이터가 있을때
- SEO를 위해 사전 렌더링 되어야만 하는 페이지일때

### TypeScript와 사용하기

next 패키지에서 `GetStaticProps` 를 import하여 타이핑해준다.
```ts
port { GetStaticProps } from 'next'

export const getStaticProps: GetStaticProps = async (context) => {
  // ...
}
```

props에 타이핑하고 싶다면 `InferGetStaticPropsType<typeof getStaticProps>` 를 사용할 수 있다.

```ts
import { InferGetStaticPropsType } from 'next'

type Post = {
  author: string
  content: string
}

export const getStaticProps = async () => {
  const res = await fetch('https://.../posts')
  const posts: Post[] = await res.json()

  return {
    props: {
      posts,
    },
  }
}

function Blog({ posts }: InferGetStaticPropsType<typeof getStaticProps>) {
  // will resolve posts to type Post[]
}

export default Blog
```

> 참고 : Next.js의 기본 정적 생성 시간 체한은 60초이다. 제한 시간 내에 새 페이지 생성이 완료되지 않으면 생성을 세 번 더 시도한다. 네 번째 시도가 실패하면 `staticPageGenerationTimeout` 에러가 발생하고 빌드가 중단된다. 이 설정을 변경하고 싶다면 다음과 같이 하면 된다.

```js
// next.config.js
module.exports = {
  // time in seconds of no pages generating during static
  // generation before timing out
  staticPageGenerationTimeout: 90,
}
```