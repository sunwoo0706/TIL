## 이벤트 루프

![이벤트 루프 사진](https://miro.medium.com/max/2048/1*4lHHyfEhVB0LnQ3HlhSs8g.png)

### JS 엔진

자바스크립트 엔진은 `Memory Heap`과 `Call Stack`으로 구성되어 있다.

자바스크립트는 싱글 스레드 프로그래밍 언어이다.

이 의미는 즉 `Call Stack`이 하나라는 이야기이다.

(하나하나씩 처리한다는 의미로 생각하면 될 것 같다.)

- **Memory Heap** : 메모리 할당이 일어나는 곳
    프로그램에 선언한 변수, 함수 등이 담겨져 있다.

- **Call Stack** : 코드가 실행될 때 쌓이는 곳이다. Stack으로 쌓이기 때문에 이름에 Stack이 들어간다.

### Web API

그림의 오른쪽에 있는 Web API는 JS Engine의 밖에 그려져 있다.

즉, 자바스크립트 엔진이 아니다.

Web API는 브라우저에서 제공하는 API로, DOM, Ajax, Timeout 등이 있다.

Call Stack에서 실행된 비동기 함수는 Web API에 보내고 Web API는 콜백함수를 Callback Queue에 보관한다.

### Callback Queue = Task Queue

비동기적으로 실행된 콜백함수가 보관되는 영역이다.

예를 들어 setTimeout에서 타이머 완료 후 실행되는 함수, 이벤트 리스너에 등록된 핸들러 함수(콜백 함수)등이 보관된다.

### Event Loop

Event Loop는 Call Stack과 계속 반복하여(Loop) Callback Queue의 상태를 체크하여, Call Stack이 빈 상태가 되면, Callback Queue의 첫번째 콜백을 Call Stack으로 밀어넣는다. 이러한 반복적인 행동을 틱(tick) 이라 부른다.

> 자바스크립트는 싱글 스레드 프로그래밍 언어라 한번에 하나씩 밖에 실행할 수 없다. 그러나 Web API, Callback Queue, Event Loop 덕분에 멀티 스레드처럼 보여진다.