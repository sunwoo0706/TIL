## Callback 함수

> Callback 함수를 알기 위해서는 (비)동기와 (논)블로킹의 [개념](Extra/A-Sync_Non-Blocking.md)을 알고 있어야 합니다.

독서와 커피마시기를 한다고 가정해보자. 당신이 독서를 하고 있을때 커피를 마시고 싶으면 책을 내려놓고 커피를 마시거나, 책을 한손으로 보며 커피를 마시는 일 두가지를 시행할 수 있다. 전자가 블로킹 Js에서 말하는 동기적처리이고, 후자가 논블로킹 Js에서 말하는 비동기적 처리이다.

전자의 상황에서 커피를 마시던 도중 커피맛이 너무 좋아 음미하며 커피를 마시는 시간에 극단적으로 30분을 사용했다고 치자. 그러면 그 30분의 시간 동안 당신은 책을 볼 수 없는 상태가 된다. 하지만 후자의 경우에는 커피가 너무 맛있어 음미하며 마시는 시간에 몇시간이 투자되어도 커피를 다 마실때까지 독서를 멈출 필요가 없게된다.

코드로 짜보면 다음과 같다.

```js
// 블로킹 (Js에서 동기)

console.log("독서");
console.log("커피 마시기 시작"); // 30분이 걸린다고 치자
console.log("커피 마시기 끝");
console.log("독서");
```

```js
// 논블로킹 (Js에서 비동기)

console.log("독서");
console.log("커피 마시기 시작");
setTimeout(() => {
  console.log("커피 마시기 끝");
}, 1800000); // 30분 소요
console.log("독서");
```

위 비동기적으로 처리한 로직을 보면 `setTimeout`을 사용한것을 알 수 있다.

setTimeout은 다음과 같은 방식으로 선언하는데 `setTimeout(fn, delay)`, 이때 인자로 받는 `fn` 즉 함수가 콜백함수이다.

`Callback` 함수를 `Call`과 `Back`으로 나누어 살펴보자
`Call`은 호출하다. 라는 뜻을 가지고 있고, `Back`은 되돌다. 라는 뜻을 가지고 있다. 두가지를 합치면 되돌아와서 호출하다. 가 된다.

### Callback 함수의 제어권

```js
const arr = ["이", "선", "우", "최", "고"];

const printArray = () => {
  a;
  console.log(arr.shift());
  if (!arr.length) {
    clearInterval(timer);
  }
};

const timer = setInterval(printArray, 1000);
```

`printArray` 함수를 콜백으로 `setInterval`에 넘겨주게되면 `prinArray`의 제어권은 `setInterval` 에게 넘어가게 된다.

### Callback hell

비동기로 처리할 로직이 많게 된다면 `setTimeout`과 같은 함수를 많이 사용하게 되는건 당연하다. 하지만 위에서 봤듯이 `setTimeout`과 같은 함수를 사용하게 된다면 코드 가독성이 현저하게 떨어지게 된다.

이를 해결하기 위해 세상에 등장한것이 바로 `Promise API` 이다.
