# BOM과 DOM

### BOM (Browser Object Model)

브라우저의 창이나 프레임을 프로그래밍적으로 제어할 수 있게 해주는 객체모델이다. 이를 통해서 브라우저의 새 창을 열거나 다른 문서로 이동하는 등의 기능을 실행시킬 수 있다. 전역 객체로 window가 있으며 하위 객체들로 `location`, `navigator`, `document`, `screen`, `history` 가 포함되어 있다.

BOM은 DOM의 상위 집합이다.

![https://i.stack.imgur.com/UGXeb.jpg](https://i.stack.imgur.com/UGXeb.jpg)

BOM은 DOM과 다르게 표준 명세가 존재하지 않아서 각 브라우저별로 구현방법이 상이하다.

### DOM (Document Object Model)

웹페이지를 프로그래밍적으로 제어할 수 있게 해주는 객체모델이다. 최상위 인터페이스로 Node가 있으며 이는 아래와 같은 구조로 나타난다.

![https://github.com/baeharam/Must-Know-About-Frontend/raw/main/images/frontend/dom.png](https://github.com/baeharam/Must-Know-About-Frontend/raw/main/images/frontend/dom.png)

위의 트리구조에서도 나오다시피 엘리먼트 뿐만 아니라 텍스트와 주석도 DOM 트리에 포함된다.
