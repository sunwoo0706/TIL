![StoryBook](https://media.vlpt.us/post-images/wlsdud2194/a23b7ed0-05e1-11ea-b5eb-0505e39593e9/storybook-1.png)

**Storybook**은 UI 구성 요소(컴포넌트)를 개발하기위한 오픈 소스 도구입니다.

예전에는 페이지 단위의 개발을 하였다면 요즘에는 컴포넌트 단위로 프론트엔드를 개발하고, 많은 분들이 React, Vue나 Angular를 이용하여 개발합니다.

여기서 컴포넌트는 외부에 영향을 받지 않고 독립적인 개체를 이루며 재사용가능한 단위라고 할 수 있습니다.

이러한 특성을 잘 지켜가며 컴포넌트를 개발할 수 있도록 도와주는 **오픈 소스 라이브러리**가 바로 **Storybook**입니다.

## 🤔 문제점

저와 같은 경우에는 보통 React.js를 이용하여 프론트 개발을 합니다.

하지만 항상 컴포넌트를 설계할 때, 필요한게 생길 때마다 해당 케이스에 맞게 컴포넌트를 설계하다 보니, 비슷한 기능을 가진 컴포넌트들이 생겨났고, 결과적으로 재활용성이 떨어졌습니다.

개발은 컴포넌트 단위로 진행하지만 실제 개발환경은 항상 페이지 단위로 만들어지기 때문에 어쩌면 당연히 일어날 수도 있지만
웹 개발에 있어서 재활용성이 떨어진다는 것은 생산성이 나빠지거나 추후에 리팩토링을 할 때, 과정이 커지고 복잡해질 수 있습니다.

## 📙 Storybook 소개

> Storybook is a user interface development environment and playground for UI components. The tool enables developers to create components independently and showcase components interactively in an isolated development environment.

Storybook이란 UI 컴포넌트를 위해 사용자 인터페이스 개발환경을 지원합니다. 또한, 개발자가 자주적으로 컴포넌트를 만들 수 있게 도와주고 고립된 개발환경에서 대화형으로 컴포넌트를 보여줍니다. (blah blah)

간단하게, 격리된 환경에서 컴포넌트를 만들고 UI 상에 내가 만든 컴포넌트를 볼 수 있게 해주는 라이브러리 입니다. 물론 그 밖에도 많은 기능들을 제공합니다.

또한 Storybook은 아래와 같이 컴포넌트를 이용하는 많은 플랫폼(?), 라이브러리를 지원하고 있습니다.

![지원하는것들](https://media.vlpt.us/post-images/wlsdud2194/fad4f680-05bd-11ea-8877-8fd4be31a741/storybook-provide.PNG)

### 미리보기

이 포스트에서는 React.js를 이용하여 간단한 Todo 리스트를 만들어 보면서 Storybook를 알아볼 예정입니다.

밑에 보시면 미리 작성해 놓은 Storybook이 있습니다. 컴포넌트에 넘겨줄 Props를 미리 주고 해당 컴포넌트가 어떻게 UI상에 보이는지 알 수 있습니다.

![기프](https://media.vlpt.us/post-images/wlsdud2194/eb8592f0-05c4-11ea-ba7e-9149eadac4b8/ezgif.com-resize.gif)

## 💡 제공하는 기능

Storybook에서 자체적으로 제공하고 있는 기능들이 있습니다. 그 중에서 유용하게 사용하고 있는 기능들 소개 해볼까 합니다.

### 애드온 Addons

Storybook에서 지원하는 플러그인(?) 같은 겁니다. 여러가지가 있지만 몇 가지만 이야기 하자면

React.js에서 props로 함수를 넘겨줄 때, @storybook/addon-actions을 이용하면 함수를 직접 선언하지 않고 action이라는 함수를 이용하며 props에서 받은 함수가 잘 호출되는지 알 수 있습니다.

@storybook/storyshot를 이용하면 Storybook을 이용한 스냅샷 테스팅을 진행할 수 있습니다.

[https://storybook.js.org/](https://storybook.js.org/)