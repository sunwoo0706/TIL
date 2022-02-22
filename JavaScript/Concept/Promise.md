## Promise가 무엇인가

`Promise` 란 간단하게 논블로킹 처리 (JS에서 말하는 비동기 처리)를 위해 자바스크립트에서 사용되는 객체라고 말할 수 있습니다.

### 프로미스 3가지 상태

- Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태
- Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
- Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

### Promise 처리

먼저 아래와 같이 `new Promise()` 메서드를 호출하면 대기 상태가 됩니다.

```js
new Promise();
```

`new Promise()` 메서드를 호출할 때 콜백 함수를 선언할 수 있고, 콜백 함수의 인자는 `resolve`, `reject`

```js
new Promise(function (resolve, reject) {
  // ...
});
```

콜백함수 안에서 `resolve`를 아래와 같이 실행하면 이행 상태가 됩니다.

```js
new Promise(function (resolve, reject) {
  resolve();
});
```

그리고 이행 상태가 되면 아래와 같이 `them()`을 이용하여 처리 결과 값을 받을 수 있습니다.

```js
function getData() {
  return new Promise((resolve, reject) => {
    var data = 100;
    resolve(data);
  });
}

// resolve()의 곂과 값 data를 resolvedData로 받음
getData().the(resolvedData => {
  console.log(resolvedData);
});
```

`new Promise()`로 프로미스 객체를 생성하면 콜백 함수 인자로 `resolve`와 `reject`를 사용할 수 있다고 했습니다. 여기서 `reject`를 아래와 같이 호출하면 실패 상태가 됩니다.

```js
new Promise(function (resolve, reject) {
  reject();
});
```

그리고, 실패 상태가 되면 실패한 이유(실패 처리의 결과 값)를 `catch()`로 받을 수 있습니다.

```js
function getData() {
  return new Promise(function (resolve, reject) {
    reject(new Error("Request is failed"));
  });
}

// reject()의 결과 값 Error를 err에 받음
getData()
  .then()
  .catch(function (err) {
    console.log(err); // Error: Request is failed
  });
```

> then에서 예외가 발생하면 실행을 멈추고 chain의 아래에서 catch를 찾습니다.
> catch부터 다시 실행을 시작한다랄까요

### 여러 개의 프로미스 chaining하기

프로미스의 또 다른 특징은 `then()` 메서드를 호출시 반환되는 값이 또 다른 새로운 프로미스 객체라는것입니다.
따라서, 아래와 같이 코딩이 가능합니다.

```js
function getData() {
  return new Promise({
    // ...
  });
}

// then() 으로 여러 개의 프로미스를 연결한 형식
getData()
  .then(function (data) {
    // ...
  })
  .then(function () {
    // ...
  })
  .then(function () {
    // ...
  });
```

### 프로미스의 에러 처리

프로미스 에러 처리 방법에는 다음과 같이 2가지의 방법이 있습니다.

1. `then()`의 두번째 파라미터로 에러를 처리하는 방법

```js
getData().then(handleSuccess, handleError);
```

2. `catch()`를 이용하는 방법

```js
getData().then().catch();
```

앞에서 프로미스 에러 처리 방법 2가지를 살펴봤습니다. 개개인의 코딩 스타일에 따라서 사용하는것은 자유이지만 가급적 `catch()`로 에러를 처리하는 게 더 효율적입니다.

두번째 파라미터로 에러를 처리하는 경우 첫번째 파라미터 콜백 함수 내부에서 오류가 나는 경우 오류를 제대로 잡아내지 못합니다.

그러므로 더 많은 오류 케이스를 커버하기 위해서 `catch()`를 사용하는것이 좋습니다.
