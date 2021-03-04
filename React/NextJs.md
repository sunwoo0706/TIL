# Next.js

NExt.js는 **Vercel**이라는 팀에서 개발하였습니다.

> Vercel is a cloud platform for static sites and Serverless Functions that fits perfectly with your workflow

## 왜 써야할까요?

SSR 지원하고 Vercel에서 만들어서 유지보수하고 대충 뭐하는 애인지는 알았습니다.
그럼 왜 써야할까요?

## SSR

Next.js를 사용하는 가장 큰 이유라고 생각합니다.
바로 SSR입니다.

SSR에 대해서 이해하려면 이와 반대 개념인 CSR과 싱글페이지 어플리케이션 SPA에 대해 먼저 알아야합니다.

## SPA

![pageLifcycle](https://media.vlpt.us/images/skypedanny/post/323854a8-e668-4b89-9815-2ac11f28c120/image.png)

전통적인 Page LifeCycle은 다음과 같습니다.

1. Client에서 Server로 최초의 요청을 보냅니다.
2. Server는 응답을 보내고 Client에서 화면이 보입니다.
3. Server는 이에 응답합니다.
4. 페이지가 Reload됩니다.

그러나 위와 같은 방법의 경우 사용자가 새로운 요청을 보내고 응답을 받을때마다 사용ㅈ의 페이지가 Reload되기 때문에 비용적인 측면에서 손해를 볼 수 밖에 없습니다.

따라서 위와 같은 방법을 해결할 수 있는 해결책이 바로 SPA입니다.

![CSR](https://media.vlpt.us/images/skypedanny/post/a15eb718-1532-474c-a3d3-e8a493c784f6/image.png)

React를 사용한 CSR의 동작 순서는 다음과 같습니다.

1. 서버에서 브라우저로 응답을 보냅니다.
2. 브라우저에서 JS를 다운로드 받습니다.
3. 브라우저가 React를 실행합니다.
4. 페이지가 보이고 상호작용 할 수 있습니다.

> CSR은 SSR에 비해서 초기에 전송되는 페이지(비어있음)의 로딩 속도는 빠르지만 서비스에서 필요한 데이터를 Client(브라우저)에서 추가로 요청하여 재구성해야 하기 때문에 전제적인 페이지 완료 시점은 SSR보다 느려집니다.

**CSR의 장점**

1. CSR의 컴포넌트 단위로 UI를 구성하기 때문에 재사용에 용이하고 중복을 줄일 수 있다.
2. 사용자가 페이지를 전환할 때 부드럽다.
3. 변경된 사항만 Server에 요청을 보내면 되기 때문에 비용적인 측면에서 효율적이다.

**CSR의 단점**

1. 초기 페이지 로딩이 오래걸린다.
2. SEO가 어렵다.
