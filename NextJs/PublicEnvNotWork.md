## 문제

`NextJS` 에서 `private key` 를 사용할 일이 있어서, `env` 를 사용해야 했지만 `NEXT_PUBLIC_...` 를 prefix로 붙였는데도 접근이 되지 않았다.

## 해결

문제를 해결한 방법은 아주 굉장히 비효율적이었다. stackoverflow에 검색해보아도 `NEXT_PUBLIC_...` 관련 문제밖에 없었다.
그래서 우선 `next-config.js` 에서 `env` 설정을 해주니 해결되었다.

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    privateKey: process.env.NEXT_PUBLIC_PRIVATE_KEY,
  },
};

module.exports = nextConfig;
```

하지만 왜 바로 접근이 되지 않는지 이해가 되지 않았다.

그래서 새로 next app을 파고 여러가지 케이스를 만들어 테스트 해보니, `pages` 폴더를 `src` 안에 넣었을때 `env` 에 바로 접근할 수 없는 것을 확인할 수 있었다.

[공식 문서](https://nextjs.org/docs/advanced-features/src-directory)에도 적혀있는 방식인데 이 부분이 따로 명시되어있지 않을수 없을것 같아 찾아보니

[![NextJS 공식문서 참고 자료](https://user-images.githubusercontent.com/60869316/162642397-398947e1-91b4-4b95-9b81-30dea944719e.png)](https://nextjs.org/docs/basic-features/environment-variables#environment-variable-load-order)

`src`의 자식 폴더가 아닐때에만 접근을 할 수 있다고 적혀있다.
