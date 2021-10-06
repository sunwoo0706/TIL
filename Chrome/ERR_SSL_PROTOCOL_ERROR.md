## ERR_SSL_PROTOCOL_ERROR

> the-moment 테스팅 서버와 연결하던중에 겪은 오류입니다.

`localhost` 에서 새로운 기능을 테스트하기 위해 `baseURL`을 변경후 서버를 실행시켰을때 다음과 같은 에러가 떴습니다.

![errpic](https://cdn.discordapp.com/attachments/881070017570045962/895137456305897482/2021-10-06_11.36.33.png)

### ERR_SSL_PROTOCOL_ERROR가 생기는 원인

말 그대로 SSL/TLS(https) 프로토콜 예외로 인해 발생하는 에러이다.

1. 서버(WAS)에서 낮은 버전의 SSL을 사용하는 경우
2. 서버(WAS)에서 응답한 `Cipher Suites`를 브라우저에서 처리 할 수 없는경우
3. 클라이언트가 https가 적용되지 않는 리소스에 https 프로토콜로 접근하려 할때

### 해결 방법

**1번** 서버가 낮은 버전의 프로토콜을 사용하는 경우에는 브라우저에서 낮은 버전의 프로토콜을 사용 가능하도록 옵션을 변경해 준다.

**2번** 서버에서 응답한 Cipher Suites를 브라우저에서 처리할 수 없는경우에는 두 가지 해결 방법이 있습니다.

1. IE Edge, FireFox, Opera 등등 다른 브라우저를 사용해봅니다.

   - 브라우저마다 처리할 수 있는 Cipher Suites 종류가 다릅니다.

2. 서버관리자가 수정 할 수 있는 방법으로 최신 프로토콜을 사용할 수 있도록 WAS를 업그레이드, 설정하거나, 대부분의 브라우저에서 지원하는 Cipher Suites를 사용하도록 설정합니다.

![lowerversionpotocol](https://2.bp.blogspot.com/-LRF3cr_kbFc/W_gIZKKwBOI/AAAAAAAAcXo/URyklh-bm7k3iAE6svJsN60SAtFI0p3CgCLcBGAs/s1600/IE11_advanced.PNG)

**3번** 본인의 경우가 3번이었습니다. 접근하려는 테스팅 서버에는 ssl이 적용되지 않은 상태였는데 친구가 `baseURL`을 잘못 수정하여 http"s"를 제거하지 않은 상태에서 접근하려하여 발생한 에러였습니다.

[📖](http://1004lucifer.blogspot.com/2018/11/chrome-errsslprotocolerror.html)
`참고자료`
