# 그래서 DOM이 정확하게 뭐야!!

DOM(Document Object Model)은 웹 페이지에 대한 인터페이스입니다. 기본적으로 여러 프로그램들이 페이지의 콘텐츠 및 구조, 그리고 스타일을 읽고 조작할 수 있도록 API를 제공합니다. 먼저 DOM을 이해하기 전에 웹 페이지가 어떻게 빌드 되는지 살펴보겠습니다.

CSSOM이라는것도 있습니다.
CSS Object Model은 JavaScript에서 CSS를 조작할 수 있는 API 집합입니다. HTML 대신 CSS가 대상인 DOM이라고 생각할 수 있으며, 사용자가 CSS 스타일을 동적으로 읽고 수정할 수 있는 방법입니다.

웹 브라우저가 원본 HTML 문서를 읽어들인 후, 스타일을 입히고 대화형 페이지로 만들어 뷰 포트에 표시하기까지의 과정을 “Critical Rendering Path”라고 합니다. [Understanding the Critical Rendering Path](https://bitsofco.de/understanding-the-critical-rendering-path/) 에서 다루듯이 이 과정은 여러 단계로 나누어져 있지만, 이 단계들을 대략 두 단계로 나눌 수 있습니다. 첫 번째 단계에서 브라우저는 읽어들인 문서를 파싱하여 최종적으로 어떤 내용을 페이지에 렌더링할지 결정합니다. 그리고 두 번째 단계에서 브라우저는 해당 렌더링을 수행합니다.

CRP에 대한 지식은 사이트의 성능을 개선 할 수 있는 방법을 이해하는 데 매우 유용합니다.CRP에는 6단계가 있습니다.

1. DOM 트리 구성
2. CSSOM 트리 구성
3. JavaScript 실행
4. 렌더 트리 만들기
5. 레이아웃 생성
6. 페인트 등
