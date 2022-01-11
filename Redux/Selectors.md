## Redux Selector

> "Selectore" 는 Redux의 state를 인수로 받고 해당 state에서 파생된 데이터를 반환하는 함수이다.

### 왜 써야 할까?

Redux store state를 최소로 유지하고 필요에 따라 state에서 데이터를 파생시키는 것이 설계의 아주 좋은 경우다. Selector는 파생된 데이터를 계산할 수 있어 Redux가 가능한 최소한의 state를 저장할 수 있게 도와주며, 인수가 변경되지 않는 한 다시 계산되지 않기 때문에 효율적이다.

### 예시

아래는 store에서 user lists를 꺼내오는 간단한 선택자이다.

```js
selectUsers = state => state.users;
```

사용자 ID를 가져와 위의 선택기를 약간 더 복잡하게 만들 수 있다.

```js
selectUserIds = state => state.users.map(user => user.id);
```

아래는 훠얼씬 복잡한 선택기이다.

```js
selectUserIdsOfName = (state, name) => state.users.filter(user => user.name === name);
```

Selectors 함수명에 Selector를 포함시키는것이 좋다. select를 접두사로 사용하는 것을 선호하지만 Selector를 접미사로 사용하는 것도 일반적이다. (selectUserIds 대신 userIdsSelector)

또한 Selector를 적합한 Reducer 근처에 두는 것이 일반적이다. 이렇게 하면 state의 형태를 변경하면 Selector또한 변경사항이 필요하므로 같은 관심사에 포함시키는것이 유지보수하기 편하다.

### 요약

Selector는 Redux state를 인수로 받아들이고 해당 상태에서 차생된 데이터를 반환하는 함수이다. Selecto는 앱의 성능 최적화를 제공하고, 전역 상태 트리를 캡슐화하는데 도움이 될 수 있다. 앱이 커지고 다루기 힘든 경우 고유한 Selector를 만들거나 메모이징되는 Selector를 제공하는 Reselect같은 라이브러리를 사용할 수 있다.