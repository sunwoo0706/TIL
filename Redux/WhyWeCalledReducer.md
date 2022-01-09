## 왜 우리는 reducer를 reducer라고 할까?

`Array.reduce()` 메서드를 사용하면 값 배열을 가져와서 배열의 각 항목을 한 번에 하나씩 처리하여 단일 최종 결과를 반환할 수 있다. 한 마디로 배열을 하나의 값으로 줄이는 것 이라고 생각할 수 있다.
`Array.reduce()` 배열의 각 항목에 대해 한 번 호출되는 콜백 함수를 인수로 사용한다. 두 가지 인수가 필요하다

- `previousResult` : 이전에 콜백이 반환한 값
- `currentItem` : 배열의 현재 항목

처음 콜백이 실행될때, `previousResult` 는 사용할 수 없다. 따라서 첫 번째 이전 결과로 사용될 초깃값을 전달해야 한다.

총계가 무엇인지 알아내기 위해 숫자 배열을 더하고 싶다면 다음과 같은 reduce 콜백을 작성할 수 있다.

```js
const numbers = [2, 5, 8]

const addNumbers = (previousResult, currentItem) => {
  console.log({ previousResult, currentItem })
  return previousResult + currentItem
}

const initialValue = 0

const total = numbers.reduce(addNumbers, initialValue)
// {previousResult: 0, currentItem: 2}
// {previousResult: 2, currentItem: 5}
// {previousResult: 7, currentItem: 8}

console.log(total)
// 15
```

Redux의 reducer 함수는 `addNumbers` 즉 `reduce callback` 과 정확히 같다. `reduce callback`은    `previous result` (state)와 `current item` (action 객체)을 인자로 취하여 해당 인수를 기반으로 새 상태 값을 결정하고 해당 새 상태를 반환한다. (그냥 뺴박)

Redux의 방법을 reduce로 구현해보면 

```js
const actions = [
  { type: 'counter/increment' },
  { type: 'counter/increment' },
  { type: 'counter/increment' }
]

const initialState = { value: 0 }

const finalResult = actions.reduce(counterReducer, initialState)
console.log(finalResult)
// {value: 3}
```

과 같이 동일한 방식으로 최종 결과를 얻을 수 있다.

Redux의 reducer는 시간이 지남에 따라 일련의 작업을 단일 상태로 줄인다고 말할 수 있다. 차이점은 reduce 메써드는 모든 것이 함수를 호출할때 한번에 일어나지만 Redux에서는 런타임으로 발생한다는것에 있다.