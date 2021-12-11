## Shadow DOM

HTML 문서의 모든 요소와 스타일로 이루어진 DOM은 하나의 큰 글로벌 범위 내에 있다.
그래서 페이지의 요소가 문서 내에 깊이 중첩되어 있거나 어디에 배치되어있는지 상관없이 `querySelector` 같은 메서드를 사용하여 접근이 가능하다. 마찬가지로 CSS 스타일 또한 글로벌 범위 내의 어떤 요소든 선택이 가능하다.

문서 전체에 스타일을 일괄 적용하고 싶은 때 이러한 방식은 매우 유용하다. 예를 들어, `box-sizing` 속성을 사용한 한 줄의 코드를 통해 페이지에 있는 모든 단일 요소를 선택 가능하다.

```css
* { box-sizing: border-box }
```

반면에 어떤 요소는 완전한 캡슐화를 필요로 하는 경우가 있고, 이것이 글로벌 스타일에 영향을 받는 것을 원하지 않을 수 있다. 이에 대한 좋은 예는 iframe으로 외부에서 가져온 위젯을 예로 들 수 있다. 이 요소또한 다음과 같이 작은 문서를 로드할 수 있다.

![트위터iframe예시](https://wit.nts-corp.com/wp-content/uploads/2019/03/-3)

`<iframe>` 은 호스팅 문서의 전역 CSS에 영향을 받지 않고 의도된 스타일을 보장할 수 있는 방법이다. 같은 결과를 얻기 위해 캐스케이드를 이용할 수 있지만, 다른 방법으로는 `<iframe>` 과 같은 보장이 주어지지 않으며 이상적인 방법은 아니다.

Shadow DOM은 `<iframe>` 과 같은 도구에 의존할 필요 없이, __웹 플랫폼에서 기본적으로 캡슐화와 구성요소화를 허용하기 위해 만들어졌다.__

### DOM 안에 DOM?

Shadow DOM을 DOM의 하위 요소로 생각할 수도 있지만, 원래의 DOM 트리에서 완전히 분리된 고유의 요소와 스타일을 가진  DOM 트리입니다. Shadow DOM은 웹 작성자가 사용하도록 최근에 지정되었지만, 사용자 에이전트에서 폼 요소와 같이 복잡한 구성요소를 만들고 스타일을 입히기 위해 수년 동안 사용되어 왔다.

예를 들어 범위 입력 요소를 살펴보자. 페이지에 해당 요소를 생성하기 위해서는 아래의 코드를 추가해야 한다.

```html
<input type="range">
```

![inputrange](https://wit.nts-corp.com/wp-content/uploads/2019/03/-4)

더 깊게 파고들면, `<input>` 요소가 실제로 여러 작은 `<div>` 요소로 구성되어 트랙과 슬라이더를 자체적으로 제어하는 것을 볼 수 있다.

![inputshadowdom](https://wit.nts-corp.com/wp-content/uploads/2019/03/-5)

이처럼 Shadow DOM을 사용하여 위와 같은 결과를 얻을 수 있다. 호스트 HTML 문서에는 단순한 `<input>` 요소가 노출되지만, 그 내부에는 DOM의 글로벌 범위에 포함되지 않는 HTML 요소와 스타일 구성 요소들이 있다.

### 어떻게 작동하는가

먼저 `<iframe>` 대신 shadow DOM을 사용하여 트위터의 "follow" 버튼을 만들어 보지.

먼저 **shadow host**로 시작합니다.

shadow host는 새로운 shadow DOM을 붙일 원본 DOM의 일반 HTML 요소를 사용합니다. Follow 버튼과 같은 구성요소의 경우, 페이지에 Javascript가 활성화되지 않았거나 shadow DOM이 지원되지 않을 경우 포시할 fallback 요소를 포함할 수 있다.

```html
<span class="shadow-host">
    <a href="https://twitter.com/ireaderinokun">
        Follow @ireaderinokun
     </a>
</span>
````

주로 상호 작용하는 특정 요소들은 shadow host가 될 수 없기 때문에, 단순하게도 `<a>` 요소를 shadow host로 사용할 수 없다.
shadow host에 shadow DOM을 붙이기 위해, `attachShadow()` 메서드를 사용한다.

```html
const shadowEl = document.querySelector(".shadow-host");
const shadow = shadowEl.attachShadow({mode: 'open'});
```

이 코드는 shadow host의 자식 요소인 빈 `shadow root`를 생성합니다. `<html>` 요소가 DOM의 시작인 것처럼 shadow root는 shadow DOM의 시작점 역할을 한다.

![shadowdom](https://wit.nts-corp.com/wp-content/uploads/2019/03/-8)

일반 HTML 자식 요소는 검사기에서 확인될지라도 shadow root가 차지하면서 더 이상 페이지에 보이지 않게 됩니다.
다음으로, 새로운 shadow tree를 만들기 위해 콘텐츠를 생성해야 합니다. shadow tree는 DOM tree와 비슷하지만 일반 DOM 대신 shadow DOM을 사용합니다. follow 버튼을 생성하기 위해서는 이미 가지고 있는 폴백 링크와 거의 동일하지만 아이콘이 있는 새로운 `<a>` 요소가 필요합니다.

```html
const link = document.createElement("a");
link.href = shadowEl.querySelector("a").href;
link.innerHTML = `
    <span aria-label="Twitter icon"></span>
    ${shadowEl.querySelector("a").textContent}
`;
```

DOM과 같은 방법으로 `appendChild()` 메서드를 사용하여 shadow DOM에 새로운 요소를 추가합니다.

```js
shadow.appendChild(link);
```

### DOM 과 Shadow DOM

어떤 면에서 shadow DOM은 DOM의 "lite" 버전입니다.
DOM과 같이 HTML 요소의 구조화된 표현이며, 페이지에 무엇을 표시할지 결정하고 요소의 수정을 가능하게 합니다. 하지만 DOM과 다르게 완전한 독립 문서를 기반으로 하지 않습니다.
이름에서 알 수 있듯이 shadow DOM은 항상 일반 DOM 내의 요소에 부착됩니다. DOM이 없으면 shadow DOM도 존재하지 않습니다.
