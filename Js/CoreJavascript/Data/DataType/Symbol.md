# Symbol

> 사람은 간혹, 한 개념을 공부할때 다른것들에 비해 굉장한 시간이 필요할때가 있죠.
> 저한테는 그게 Symbol 이었습니다!! 😡

여러분들은 그런 고생하시지 마라고 아주 간단하게 설명드릴게요..

우선 사용방법에 대해서 먼저 알려드리도록 하겠습니다.

```js
const symbol1 = Symbol();
const symbol2 = Symbol(42);
const symbol3 = Symbol("foo");

console.log(typeof symbol1);
// expected output: "symbol"

console.log(symbol2 === 42);
// expected output: false

console.log(symbol3.toString());
// expected output: "Symbol(foo)"

console.log(Symbol("foo") === Symbol("foo"));
// expected output: false
```

이런식으로 사용합니다.

네 무슨 소리인지 모르시겠죠. 저 또한 그랬습니다.
제가 이해한 내용을 바탕으로 아주 간단하게 설명드리도록 하겠습니다.

> 한 마디로 다른 모듈에서 접근할 수 없게 만들어주는 겁니다.

다른 언어에 비유한다면 private 이라던지가 있지요. (전 여기서 이해가 되었어요. 역시 비유가 짱)

근데 또 아예 접근을 못하는게 아니예요.

그러니까 코드 가독성을 높여주는 개념으로 생각하시면 됩니다.
그리고 저렇게 함수로 선언을 할때 안에 문자열이나 숫자를 넣을수가 있는데 저건 일종의 주석으로 보시면 될 것 같습니다.

그렇다고 아예 또 아무 기능이 없는것도 아니예요.(슬슬 화가 납니다.)

이를테면 어떠한 라이브러리를 만들고 그걸 상속시켜주었을때 변수같은것들이 가끔씩 덮쳐질때가 있죠. 그런것을 막아주는게 Symbol의 역할입니다.
