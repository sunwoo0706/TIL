## Recoil

📌 **리코일 설명**

> ### 리코일의 탄생 동기
>
> 리덕스에 대한 불만
>
> ![](https://media.vlpt.us/images/wooder2050/post/04c09a7c-7e37-4475-ae7d-353a7712e991/redux1.png)
>
> 위 그림은 상태 관리 라이브러리의 만족도에 대한 조사결과이다. 리덕스의 만족도는 급격하게 떨어졌고 3년 이후 사라진 기술 1위로 리덕스가 꼽혔다.

> ### Recoil이란 무엇인가?
>
> **A state management library for react**
>
> **We want to improve this while keeping both the API and the semantics and behavior as Reactish as possible.**
>
> Recoil은 API, 의미, 동작을 최대한 _리액트스럽게_ 유지하며 이를 개선하고자 한다.

📌 **리코일 시작하기**

> ### Atom
>
> ![](https://media.vlpt.us/images/wooder2050/post/a0987f2c-5523-4892-8d41-6618dac62c6f/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.16.34.png)
>
> `Atom`은 상태이다. 리액트의 state, props 와 비슷하지만 리덕스의 store의 상태들처럼 구독할 수 있고 `Atom`의 상태가 변경되면 구독하고 있는 컴포넌트들의 다시 렌더링되면서 변경된 `Atom`의 상태를 공유한다.
>
> ![](https://media.vlpt.us/images/wooder2050/post/e9d5c853-349a-4dbb-83c9-1af58b6d5f4d/atomex.png)
>
> `Atom`은 고유한 키값과 기본값을 가진다. 고유한 키값을 이용해서 필요한 컴포넌트에서 `Atom`를 사용할 수 있고 기본값은 초기값이 된다.
>
> ### useRecoilState
>
> ![](https://media.vlpt.us/images/wooder2050/post/a277bfa1-c3d8-4ff9-ba4a-43885d7c11d4/useRecoilStateEx.png)
>
> `useRecoilState`은 hook의 `useState`와 사용하는 방식이 동일하다. 배열 첫번째 요소에 상태의 값이 들어가고 두번째 요소에 상태를 변경할 수 있는 함수가 들어간다. 차이점은 이 변경된 상태가 자동으로 전역으로 상태가 공유된다는 것이다. 구독이나 연결과 같은 작업은 필요없다. `useRecoilState`을 사용한 `Atom`의 상태는 이 상태를 사용하고 있는 다른 컴포넌트와 자동으로 공유된다.
>
> ### useRecoilValue
>
> ![](<https://media.vlpt.us/images/wooder2050/post/4569de9a-31da-4964-8e32-c6548b24ac7b/carbon%20(2).png>)
>
> `useRecoilValue`는 상태를 변경하는 함수없이 `Atom` 값만 받는다.
>
> ### selector
>
> ![](https://media.vlpt.us/images/wooder2050/post/cc89b51b-d3b5-4a27-9212-00ed0c695e78/selector.png)
>
> ![](https://media.vlpt.us/images/wooder2050/post/5358d33e-9b7b-455d-ab2e-260e2a5a091f/selector3.png)
>
> 여러 상태를 이용해 값을 표현할때가 있다. 이러한 상황에서는 각각의 상태가 변경될 때, 아 값 또란 즉각적으로 변경되어야 한다.
> `selector`는 [pure function](../../../Etc/PureFunction)으로서 `Atom`이나 또 다른 `selector`를 이용해서 새로운 데이터를 전달해줄 수 있다. `selector`를 이용하면 연관된 `Atom`과 `selector`가 변경되면 그에 따른 변경된 값을 즉시 받을 수 있고 이 `selector`를 사용하는 컴포넌트도 다시 렌더링된다. `selector`에서는 `async`를 이용해 비동기 작업 또한 가능하다. 서버에서 api로 데이터를 불러오는 것도 가능하다.
>
> ![](https://media.vlpt.us/images/wooder2050/post/bdddf32f-dee0-4fc5-bc2d-9ea66a40a4ff/select.png)
>
> `selector` 또한 고유한 키값을 갖는다. `get`에는 반환 값을 만들어주면 된다. 위에 예시에는 `cartState`, `shippingState`를 이용해서 최종 가격을 연산하는 로직을 만들었다.
>
> ![](<https://media.vlpt.us/images/wooder2050/post/635e7e23-8020-4ecb-b65e-ea147abc014b/carbon%20(3).png>)
>
> 사용할 컴포넌트에서는 `useRecoilValue`를 이용해서 `get`에서 리턴되는 값을 받으면 된다. 아직까지는 `selector`를 `useRecoilState`와 함께 사용할 수 없다. `selector`의 값은 읽기전용으로만 사용 가능하다.(추후에 업데이트 될지도?)
