# 나무흔들기 (Tree shaking)란?

트리쉐이킹은 쉽게 말해 번들파일의 불필요한 코드를 제거해주는 것을 말한다. 나무를 흔들어서 말라 죽은 잎들을 떨어트리는 것을 비유해서 지은 이름이다.

웹팩에서는 기본적으로 트리쉐이킹을 제공해주지만, 모든 경우에서 작동이 잘 되는 것은 아니다.

그래서 웹팩의 트리쉐이킹을 잘 이해해야 번들파일의 크기를 최소화 할 수 있다.

> 한마디로 쓸모없는 소스코드를 털어주는 작업

## ESM이 아닐 때

트리쉐이킹은 ESM(ECMAscript Module)이 아닐 때 트리쉐이킹은 실패한다.

사용되는 모듈이 ESM이 아니거나 **사용하는 쪽에서 ESM 이 아닌 다른 모듈 시스템을 사용해도** 트리쉐이킹이 제대로 이루어지지 않는다.

`util_ESM.js`

```js
export function func1() {
  console.log("func1");
}
export function func2() {
  console.log("func2");
}
```

`util_common.js`

```js
function func1() {
  console.log("func1");
}
function func2() {
  console.log("func2");
}

module.exports = { func1, func2 };
```

---

`npx webpack` 실행 후

### 트리쉐이킹 성공

`index.js``

```js
import { func1 } from "./util_ESM";
func1();
```

> 트리쉐이킹이 제대로 이루어져 사용되지않은 `func2` 함수가 번들파일에 포함되지 않는다.

### 해당 모듈 기능만 불러오기

`index.js

```js
import fill from "lodash/fill";

//...
```

> `lodash` 패키지에서 `fill` 함수만 불러왔다.

### 제공해주는 ESM 패키지 사용하기

> `lodash-es` 가 ESM이라 트리쉐이킹이 잘 동작한다.

## 바벨 사용시

바벨로 컴파일을 했을 때 작성한 코드가 ESM 모듈 문법으로 남아있어야 트리쉐이킹이 제대로 이루어진다.

만약 `@babel/preset-env` 플러그인을 사용한다면 `babel.config.js` 파일에서 다음과 같이 설정해야한다.

`babel.config.js`

```js
const presets = [
  "@babel/preset-env",
  {
    // ...
    modules: false,
  },
];
```

> `modules`를 false로 설정하면 ESM 모듈 문법을 유지하게 되어 트리쉐이킹에 영향을 주지 않는다.
