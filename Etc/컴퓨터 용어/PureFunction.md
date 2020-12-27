## 순수 함수

```js
function add(a, b) {
  return a + b;
}
console.log(add(10, 5));
```

add는 순수함수다.

언제, 어디서 실행해도 add(10,5)는 항상 15를 리턴하고 외부 상태를 변경하지 않았기 때문이다.
