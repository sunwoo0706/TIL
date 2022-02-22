## async await

이 글은 비동기 처리와 Promise에 대한 이해 기반이 깔려있다는것을 전제로 작성한 글입니다.
아직 이해하지 못했다면 읽고 와주세요. [Callback](./Callback.md), [Promise](./Promise.md)

`async`와 `await`은 자바스크립트의 비동기 처리 패턴 중 가장 최근에 나온 문법이다. 기존의 비동기 처리방식인 콜백 함수와 프로미스의 단점을 보완하고 사용시 높은 가독성을 가진 코드를 작성가능하다.

개발자들은 위에서부터 아래로 한 줄 한줄 차근히 읽으면서 사고하는 것이 편합니다. 그렇게 프로그래밍을 배웠으니까요.

콜백은 위 사항에 반하죠

```js
function logName() {
  // 아래의 user 변수는 위의 코드와 비교하기 위해 일부러 남겨놓았습니다.
  var user = fetchUser("domain.com/users/1", function (user) {
    if (user.id === 1) {
      console.log(user.name);
    }
  });
}
```

콜백을 모르는 사람이라면 위 코드를 보고 갸우뚱하게 될 것 이다.

그래서 개발자들이 처음 프로그래밍을 배웠던 그때 그 사고로 돌아가자는것이다. 아래와 같이 간단하게 생각해보자

```js
// 비동기 처리를 콜백으로 안해도 된다면..
function logName() {
  var user = fetchUser("domain.com/users/1");
  if (user.id === 1) {
    console.log(user.name);
  }
}
```

서버에서 사용자 데이터를 불러와서 변수에 담고, 사용자 아이디가 1이면 사용자 이름을 출력한다.

이렇게 하려면 `async` `await`만 붙이시면 됩니다.

```js
async function logName() {
  var user = await fetchUser("domain.com/users/1");
  if (user.id === 1) {
    console.log(user.name);
  }
}
```

### async await의 기본 문법

```js
async function 함수명() {
  await 비동기_처리_메서드_명();
}
```

먼저 함수의 앞에 `async`라는 예약어를 붙인다. 그러고 나서 함수의 내부 로직 중 HTTP 통신이나 파일읽기등 비동기 처리 코드 앞에 `await`을 붙인다. 여기서 주의할점은 비동기 처리 메서드가 꼭 프로미스 객체를 반환해야 `await`가 의도한 대로 동작한다.

`await`를 사용하지 않았다면 데이터를 받아온 시점에 콘솔을 출력할 수 있게 콜백 함수나 `.then()`등을 사용해야 했을 겁니다. 하지만 `async` `await` 문법 덕택에 비동기에 대한 사고를 하지 않아도 되는 것이죠.

### async await 예외 처리

`async` & `await`에서 예외를 처리하는 방법은 바로 `try catch`입니다. 프로미스에서 에러 처리를 위해 `.catch()`를 사용했던 것처럼 `async`에서는 `catch {}` 를 사용하시면 됩니다.
