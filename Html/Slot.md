## Slot

> [Shadow DOM](./ShadowDom.md) 에 대해서 공부중 추가로 slot에 대해서 알게 되었고, 더불어 svelte의 slot 개념과 같은것 같아 공부한다.

슬롯은 사용자가 컴포넌트 내부에 원하는 마크업을 채울 수 있도록 미리 선언해놓은 **자리 표시자**라고 할 수 있다.
주로 사용자 커스텀 요소를 생성할 때 유용합니다. 사용자 커스텀 요소에 필요한 최소한의 마크업만 제공하고, 작성자가 원하는 대로 그룹화하고 스타일을 적용하여 사용할 수 있다.
슬롯을 설명하기 전에 `<template>`을 사용한 마크업 예시를 먼저 살펴보자

```html
<!-- 렌더링할 템플릿 선언 -->
<template id="my-template">
    <style>
        p { color: green; }
    </style>
    <p>Hello, Shadow DOM!</p>
</template>
<!-- 사용자 커스텀 요소 사용 -->
<my-template></my-template>
```

```js
// 사용자 커스텀 요소를 정의하고 준비한 템플릿 코드를 가져와 shadow DOM을 생성한다.
// shadow DOM으로 인해 템플릿 내의 코드는 캡슐화된다.
class myTemplate extends HTMLElement {
    constructor() {
      super();
      let template = document.getElementById('my-template');
      let templateContent = template.content;
      const shadowRoot = this.attachShadow({mode: 'open'})
            .appendChild(templateContent.cloneNode(true));
    }
}
customElements.define('my-template', myTemplate);
```

템플릿 요소는 마크업 조각 형태로 이루어집니다. 이는 페이지 로딩 시 렌더링 되지 않으며 자바스크립트를 이용해 런타임 시 인스턴스화할 수 있다.
따라서 자주 사용되는 마크업 조각들을 템플릿 요소에 추가하고 복제함으로써 재사용성을 증가시킨다. 또한 템플릿 요소가 shadow host로 지정되어 내부 스타일을 가질 수 있다.
하지만 템플릿은 단순히 작성된 요소만 화면에 표시하기 때문에 유연하지 않다. 슬롯은 이러한 템플릿 코드에 유연성을 제공합니다.
슬롯을 사용한 템플릿 코드 예시를 살펴보겠다.

```js
<!-- 빈 슬롯이 추가된 템플릿 선언 -->
<template id="my-template">
    <style>
        :host { color: green; }
    </style>
    <slot></slot>
</template>
<!-- 각각의 사용자 커스텀 요소마다 다른 요소를 삽입  -->
<my-template>
     <h1>Hello Shadow DOM!</h1>
</my-template>
<my-template>
     <p>Hello, Shadow DOM!</p>
</my-template>
```

하나의 슬롯을 사용했지만, 결과적으로는 다른 두 요소를 렌더링한다.

![slot ex](https://wit.nts-corp.com/wp-content/uploads/2019/03/-11)

### named slot

다양한 콘텐츠로 이루어진 복잡한 요소는 명명된 슬롯을 사용하여 쉽게 생성할 수 있습니다. 슬롯을 통해 다양한 요소들이 하나의 템플릿에서 구현 가능하므로 매우 유용합니다.

```html
<!-- 템플릿 선언 -->
<template id="my-template">
    <slot name="title"></slot>
    <hr>
    <slot></slot>
</template>
<!-- 사용자 커스텀 요소 -->
<my-template>
     <h1 slot="title">제목</h1>
     <p>이 텍스트는 이름 없는 빈 슬롯에 들어가게 됩니다.</p>
</my-template>
```

![명명된 슬롯 표시](https://wit.nts-corp.com/wp-content/uploads/2019/03/-10)

> 참고 : `<my-template>` 내의 `<h1>`, `<p>`과 같은 자식 요소들을 Light DOM이라고 합니다. 이들은 템플릿 코드에 있는 지정된 slot을 찾아갑니다.

### 스타일

스타일 지정
웹 구성 요소와 shadow DOM 내부 요소에 스타일을 지정하는 다양한 방법이 있습니다.

:host : shadow root로 지정된 웹 구성 요소에 스타일을 적용합니다.
:host-context(<selector>) : 웹 구성 요소 혹은 상위 요소의 선택자가 <selector>와 일치하면, 웹 구성 요소의 자식 요소에 스타일을 적용합니다.
::slotted(<compound-selector>) : 지정한 복합 선택자와 일치하는 슬롯 콘텐츠에 스타일을 적용합니다.

간단한 예시를 살펴보면,

```html
<!-- 템플릿 선언 -->
<template id="my-template">
    <style>
        :host {
            all: initial;
            display: block;
            contain: content;
            color: green;
        }
        :host(:hover) {
            border: 1px solid blue;
        }
        :host-context(.orange-theme) {
            color: orange;
        }
        ::slotted(a) {
            color: red;
            text-decoration: none;
        }
    </style>
    <slot></slot>
</template>
<!-- 사용자 커스텀 요소 -->
<my-template>
    <h1>Hello Shadow DOM!</h1>
</my-template>
<my-template class="orange-theme">
    <div>
        <span>text 1</span>
        <span>text 2</span>
        <span>text 3</span>
    </div>
</my-template>
<my-template>
    <a href="#">Hello, Shadow DOM!</a>
</my-template>
```

![스타일 적용 예시](https://wit.nts-corp.com/wp-content/uploads/2019/03/-9)