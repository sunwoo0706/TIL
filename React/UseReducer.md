## useReducer

상태를 관리하게 될 때 useState를 사용하는것 말고도 다른 방법이 있다. 그것이 바로 주제인 useReducer이다.

이 Hook을 쓰게 되면 컴포넌트의 상태 업데이트 로직을 컴포넌트에서 분리할 수 있다.

### reducer

reducer는 현재 상태와 액션 객체를 파라미터로 받아와서 새로운 상태를 반환해주는 함수이다.

```js
function reducer(state, action) {
  // 새로운 상태를 만드는 로직
  // const nextState = ...
  return nextState;
}
```

reducer 에서 반환하는 상태는 곧 컴포넌트가 지닐 새로운 상태가 된다.

여기서 action은 업데이트를 위한 정보를 가지고 있다. 주로 type 값을 지닌 객체 형태로 사용하지만, 꼭 따라야 할 규칙은 따로 없다.

```js
// 카운터에 1을 더하는 액션
{
  type: 'INCREMENT'
}
// 카운터에 1을 빼는 액션
{
  type: 'DECREMENT'
}
// input 값을 바꾸는 액션
{
  type: 'CHANGE_INPUT',
  key: 'email',
  value: 'tester@react.com'
}
// 새 할 일을 등록하는 액션
{
  type: 'ADD_TODO',
  todo: {
    id: 1,
    text: 'useReducer 배우기',
    done: false,
  }
}
```

위 처럼 action 객체의 형태는 자유다. type 값을 대문자와 _로 구성하는 관습이 존재하지만, 위에서도 말했듯이 꼭 따라야 할 필요는 없다.

### 사용법

```js
const [state, dispatch] = useReducer(reducer, initialState);
```

여기서 state 는 우리가 앞으로 컴포넌트에서 사용 할 수 있는 상태를 가르키게 되고, dispatch는 액션을 발생시키는 함수라고 이해하면 된다. 

dispatch는 다음과 같이 액션을 파라미터로 넘겨줘서 사용한다.

```js
dispatch({ type: 'INCREMENT' })
```

그리고 useReducer 에 넣는 첫번째 파라미터는 reducer 함수이고, 두번째 파라미터는 초기 상태이다.