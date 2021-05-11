## useHistory

📌 **useHistory 설명**

> - react-router-dom 5.1v 이상 버전부터 지원됩니다.

> useHistory는 `history`를 쉽게 다룰 수 있게 해줍니다.
>
> 여기서 `history`란 세션 기록을 관리하기위한 여러 가지 구현을 제공하는 패키지입니다.
> **Home**을 컴포넌트로 지정하고 있는 Route 태그의 부모 요소인 **BrowserRouter**, **Switch**에 의해서 Home 컴포넌트의 **defaultProps** 에는 **history** 객체가 들어가게 되고, 이 **history** 객체를 이용하여 리액트 어플리케이션 내에서 라우팅이 가능합니다.
> 그리고 **history** 객체를 사용하기 위해서는 **withRouter hoc**를 이용하여 컴포넌트를 감싸주어야 작동을 합니다.

> 예시 코드 :
>
> ```js
> import React from 'react';
> import { withRouter } from 'react-router-dom';
>
> const Home = ({ history }) => {
>   return (
>     <div onClick={() => history.push('/auth')}>Hello!<div>
>   );
> };
>
> export default withRouter(Home);
> ```

> 이렇게 하게 된다면 여러 문제가 발생할 수 있는데 이때 쓰는것이 바로 `useHistory hook`이다.
>
> `useHistory`는 일반적인 `history` 객체와 똑같은 객체를 가지므로 사용법이 동일하며, 사용하기 위한 준비단계는 거의 없습니다. ( `withRouter hoc`를 사용하지 않아도 됩니다. )

📌 **useHistory 사용방법**

> 예시 코드 :
>
> ```js
> import React from "react";
> import { useHistory } from "react-router-dom";
>
> const Home = (): JSX.Element => {
>   const history = useHistory();
>   // history를 props에서 얻어왔을 때 처럼 동일하게 사용 가능하다.
>
>   return (
>     <div onClick={() => history.push("/auth")}>
>       <div>Hello!</div>
>     </div>
>   );
> };
>
> export default Home;
> // withRouter hoc가 필요없다.
> ```

> 이런식으로 훅을 선언해주고 `.push("{이동하고싶은 경로}")`를 써서 간단하게 사용가능하다.
