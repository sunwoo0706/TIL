## ERR_CONNECTION_REFUSED

> the-moment 테스팅 서버와 연결하던중에 겪은 오류입니다.

`localhost` 에서 새로운 기능을 테스트하기 위해 `baseURL`을 변경후 서버를 실행시켰을때 다음과 같은 에러가 떴습니다.

![ERR_CONNECTION_REFUSED](https://cdn.discordapp.com/attachments/731071732172980284/895135479526227998/2021-10-06_11.28.44.png)

### ERR_CONNECTION_REFUSED가 생기는 원인

`ERR_CONNECTION_REFUSED`은 오류! 연결 거부! 라고 해석할 수 있습니다.

`ERR_CONNECTION_REFUSED`은 메시지는 웹 사이트가 호스팅 되는 서버가 요청하게 되는데 해당 웹페이지를 서비스하는 웹 서버에서 웹 서비스를 제공하지 못하면 Google 크롬에 `ERR_CONNECTION_REFUSED`라는 오류 메시지가 표시됩니다.

1. IP 주소에 문제가 있을 경우
2. ISP에 문제가 있을 경우

### 해결 방법

**1번** 본인의 경우가 1번이었습니다. IP주소에 문제가 있을 경우는 IP주소를 확인하고 옳은 IP주소를 바꾸는 방법이 있습니다.<br />
그리고 특히 port가 정확한지 확인해야합니다.
저의 경우 같이 작업하는 멤버가 port 번호를 붙이지 않아서 발생한 에러였습니다.

**2번** 이 경우에는 좀 복잡한데 ISP에 문제가 있을 경우에는 VPN또는 프록시 서버를 사용하여 접근하여야합니다.<br />만약 이 경우에 해당된다면 DNS 캐시를 비워야 합니다.
