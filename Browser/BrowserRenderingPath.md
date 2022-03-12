## 브라우저 렌더링 과정

브라우저가 화면에 나타나는 요소를 렌더링 할 때, 웹킷(Webkit)이나 게코(Gecko) 등과 같은 렌더링 엔진을 사용한다. 렌더링 엔진이 HTML, CSS, JS로 렌더링할 때 CRP 라는 프로세스를 사용하며 다음 단계들로 이루어진다.

1. HTML 파싱후 DOM 생성
2. CSS 파싱후 CSSOM 생성
3. Javscript 실행
4. DOM과 CSSOM을 접합한 렌더링 트리 생성
5. 뷰포트에 맞게 노드의 각각의 위치나 크기를 계산
6. 페인트

![https://blog.asamaru.net/res/img/post/2017/05/understanding-the-critical-rendering-path.png](https://blog.asamaru.net/res/img/post/2017/05/understanding-the-critical-rendering-path.png)

1. DOM 트리 구축

DOM 트리는 완전히 구문 분석된 HTML의 Object 모델이다. 루트 요소로 시작하여 elem/txt에 대한 노드가 만들어진다.

HTML에서 다른 요소 내에 중첩된 요소는 자식 노드로 표시되며 각 노드에는 해당 요소의 속성이 포함된다.

HTML은 부분적으로 실행될 수 있다.

1. CSSOM 트리 구축

CSSOM은 DOM과 연관된 스타일의 Object 모델이다.

CSS는 렌더링 차단 리소스로 간주된다. 즉, 리소스를 완전히 파싱하지 않으면 렌더링 트리를 구성 할 수 없다.

CSS는 현재 장치에 적용되는 경우에만 렌더링 차단 리소스로 간주된다.

미디어 쿼리가 해당하지 않는 경우 해당 미디어 쿼리의 스타일 시트는 렌더링 차단 리소스로 간주되지 않는다.

CSS “script blocking”일 수도 있다. 왜냐면 js파일은 CSSOM이 생성 될 때까지 기다려야 하기 때문이다.

1. Javascript 실행

JS는 파서 차단 리소스로 간주된다.

1. 렌더링 트리 구축

렌더링 트리는 DOM과 CSSOM을 조합하여 페이지에 표시되는 내용을 나타내는 트리다. display: none을 사용하여 CSS로 숨겨진 요소를 포함되지 않는다.

1. 뷰포트를 기준으로 렌더트리의 각 노드들의 위치나 크기를 계산

### CRP 최적화

자원 다운로드를 연기함으로써 주요 리소스들의 수를 최소화하기, 필수적인 요청 횟수 최적화하기, 중요 자원 불러오는 순서를 최적화하고, 중요 경로 길이를 최소화하기

### 참고 자료

---

MDN CRP : [https://developer.mozilla.org/ko/docs/Web/Performance/Critical_rendering_path](https://developer.mozilla.org/ko/docs/Web/Performance/Critical_rendering_path)

구글 CRP/렌더트리 생성 : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction)

naver 브라우저 동작 원리 : [https://d2.naver.com/helloworld/59361](https://d2.naver.com/helloworld/59361)

스택오버플로우 답변이 아주 야무짐 : [https://stackoverflow.com/questions/34269416/when-does-parsing-html-dom-tree-happen](https://stackoverflow.com/questions/34269416/when-does-parsing-html-dom-tree-happen)
