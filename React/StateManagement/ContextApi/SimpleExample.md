# ContextAPI 간단한 예제

![](https://media.vlpt.us/images/edb1631/post/518d2487-5cac-4a66-9553-c9667dcc01f8/image.png)

```ts
//UserContext.ts
import { createContext } from "react";

export type User = {
  name: string;
  age: number;
};
export type Users = User[];

const UserContext = createContext<Users | []>([]);

export default UserContext;
```

**일단 Context를 정의를 해줍니다.
Context는 하나의 상자라고 생각을 하고,
아무런 작업을 해준게 없는 지금은 Context에 접근할 수 없다는 것을
기억해주세요!**

그 다음 이 상자에 접근할 수 있는 권한을 부여할 컴포넌트를

```ts
<UserContext.Provider value={users}>
  <User />
</UserContext.Provider>
```

이렇게 감싸줍니다. value 속성에는

```ts
const users: Users = [
  {
    name: "홍준혁",
    age: 18,
  },
];
```

이렇게 데이터를 정의해줍니다.
**그 다음 User컴포넌트를 가봅시다.**

```ts
import UserContext from "contexts/User";
import { useContext, useEffect } from "react";

const User = () => {
  const user = useContext(UserContext);
  useEffect(() => {
    console.log(user);
  }, []);

  return <></>;
};

export default User;
```

이렇게 해서 콘솔창을 보면

![](https://media.vlpt.us/images/edb1631/post/91ff59b7-d84d-4c8e-a6d4-a0a7714e76dc/image.png)

정상적으로 배열이 출력되는 모습을 볼 수 있습니다.

전 일베를 혐오합니다.

[출처](https://velog.io/@edb1631/Context-API-사용하는-방법)
