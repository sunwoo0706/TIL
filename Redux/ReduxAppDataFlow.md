## Redux 앱 데이터 흐름

- 초기 설정
    - root reducer 함수를 사용하여 만들어진 Redux store가 있다.
    - store는 root reducer 함수를 한번 부르고, 반환된 값을 초깃값으로 저장한다.
    - UI가 처음으로 렌더링 될 때, UI 컴포넌트는 Redux store에 있는 현재 상태값에 접근하고, 무엇을 렌더링할지 정하기 위해 그 상태값 데이터를 사용한다. 그리고 store 업데이트를 구독하여 상태가 바뀌게 되었는지 알 수 있게 된다.

- 상태 변화
    - 앱에서 이벤트가 발생한다.
    - 앱의 코드가 Redux store에 action을 발생시킨다.
    - store가 이전 상태값과, 현재 action을 가지고 reducer를 작동시킨다. 그리고 반환된 새로운 상태값을 저장한다.
    - store는 store를 구독하고 있는 모든 UI에 store가 업데이트 되었음을 알린다.
    - store의 데이터가 필요한 각각의 UI 구성 컴포넌트는 필요한 state가 업데이트 되었는지 확인한다.
    - store의 데이터가 변경된 각각의 컴포넌트는 새 상태값으로 강제로 다시 렌더링되므로 화면에 표시된 내용을 업데이트할 수 있다.

![redux flow](https://ko.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif)