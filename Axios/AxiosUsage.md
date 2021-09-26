# GET 요청

axios를 사용해 `GET` 요청하는 방법은 다음과 같습니다.

```js
const axios = require("axios");

// ID로 사용자 요청
axios
  .get("/user?ID=12345")
  // 응답(성공)
  .then(function (response) {
    console.log(response);
  })
  // 응답(실패)
  .catch(function (error) {
    console.log(error);
  })
  // 응답(항상 실행)
  .then(function () {
    // ...
  });
```

선택적으로 위 요청은 다음과 같이 수행할 수도 있습니다.

```js
axios
  .get("/user", {
    params: {
      ID: 12345,
    },
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // ...
  });
```

## Async 함수

async/await를 사용할 경우 함수 또는 메서드 앞에 `async`키워드를 사용하고 내부에 `async`키워드를 사용해 비동기 통신 요청을 처리합니다. async/await는 요류 디버깅을 위해 try...catch 구문을 사용합니다.

```js
async function getUser() {
  try {
    const response = await axios.get("/user?ID=12345");
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

> **주의!**<br>async/await는 ECMAScript 2017(ES8)에 추가된 새로운 방법으로 IE를 포함한 오래된 브라우저는 지원하지 않습니다.

## POST 요청

axios를 사용해 `POST` 요청하는 방법은 다음과 같습니다.

```js
axios
  .post("/user", {
    firstName: "Fred",
    lastName: "Flintstone",
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```

## 멀티 요청

여러 개의 요청을 동시 수행할 경우 `axios.all()`메서드를 사용합니다.

```js
function getUserAccount() {
  return axios.get("/user/12345");
}

function getUserPermissions() {
  return axios.get("/user/12345/permissions");
}

axios.all([getUserAccount(), getUserPermissions()]).then(
  axios.spread(function (acct, perms) {
    // Both requests are now complete
  })
);
```

# POST 요청

axios를 사용해 `POST` 요청하는 방법은 다음과 같습니다.

```js
axios
  .post("/user", {
    firstName: "Fred",
    lastName: "Flintstone",
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```

# 멀티 요청

여러 개의 요청을 동시 수행할 경우 `axios.all()` 메서드를 사용합니다.

```js
function getUserAccount() {
  return axios.get("/user/12345");
}

function getUserPermissions() {
  return axios.get("/user/12345/permissions");
}

axios.all([getUserAccount(), getUserPermissions()]).then(
  axios.spread(function (acct, perms) {
    // Both requests are now complete
  })
);
```
