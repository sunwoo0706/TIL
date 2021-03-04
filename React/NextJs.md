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
