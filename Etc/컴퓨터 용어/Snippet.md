# Snippet

스니펫은 재사용 가능한 소스 코드, 기계어, 텍스트의 작은 부분을 일컫는 프로그래밍 용어이다. 사용자가 루틴 편집 조작 중 반복 타이핑을 회피할 수 있게 도와준다.

## 예

---

2개의 변수 x, y의 값을 서로 바꿔치기하는 과정을 떠올려보자. weak typing이면서 이름 충돌에 대한 걱정이 없다고 가정할 때 이것은 다음과 같은 코드로 표현된다:

```
temp = x
x = y
y = temp
```

스니펫이 삽입될 때 프로그래머는 2개의 매개변수의 값에 대해 확인을 받는다. 이 값들이 자료형 foo, bar이고 서로 바꾸고자 하는 변수의 실제 이름이라고 가정하면, 다음의 코드를 생성하게 된다:

```
temp = foo
foo = bar
bar = temp
```

스니펫이 최종적으로 변경되어 temp 대신 \_\_temp를 사용하게 되면 이미 삽입된 코드를 변경하지는 않지만 스니펫의 최종 삽입부에 사용된다.<br />
이에 대한 스니펫은 다음과 같이 표현할 수 있다:

```
temp = $1
$1 = $2
$2 = temp
```

출처 : [위키피디아](https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%8B%88%ED%8E%AB)

---

또 하나 (사실 저거 보고 이해 안가서 하나 더 적는거임)

스니펫은 파편을 뜻한다. 요즘 활용되는 왠만한 코드 편집기, IDE 등은 `code snippet`단위로 '템플릿'을 만들어 써먹을 수 있게 되어있다. 지정한 접두어를 입력하면 템플릿이 입력되는 식이다.

![설명](https://code.visualstudio.com/assets/docs/editor/userdefinedsnippets/ajax-snippet.gif)

<i>쉽게말해 자동완성을 할 수 있게 해준다!</i>

주로 썼던 vim에도 기능을 제공하는 plugin-ultisnips, vim-snippets 등-이 있지만, VSCode로 갈아탔으므로(ㅎㅎ) VSCode에서 snippet을 쓰는 방법을 알아봤다.

## VScode에서 Snippet 활용방법

File -> Preferences -> User Snippets 클릭

1. 스니펫 범위설정

2. javascript 편집하는데 c++용으로 만들어둔 스니펫이 추천되면 곤란할 것이다. 이런 상황을 막기 위해 vscode에서는 1) 언어, 2) 프로젝트 기준으로 스니펫 범위를 설정할 수 있다.
   언어 기준으로 스니펫을 설정할 경우, 1) single language 2) multi-language (global) 로 세부범위를 설정할 수 있다.
   나는 C++ 언어를 쓰는 경우에만 쓰는 snippet을 설정하고 싶었으므로, cpp.json파일을 선택하여 편집하였다.
   스니펫 내용설정

3. 이제 스니펫 내용을 cpp.json파일에 적어넣으면 된다.
   나의 경우 `*.hpp` 파일을 만들 때 파일명으로 ifndef~endif 설치, class 선언해주는 것을 간소화하기 위해 아래처럼 작성하였다.

```json
   	"setHPP": {
   		"prefix": ">setHPP",
   		"body": [
   			"#ifndef ${1:${TM_FILENAME_BASE}}_HPP",
   			"# define ${1:${TM_FILENAME_BASE}}_HPP",
   			"",
   			"class ${1:${TM_FILENAME_BASE}}",
   			"{",
   			"private:",
   			"    ${2:/* data */}",
   			"public:",
   			"    ${1:${TM_FILENAME_BASE}}(${3:/* args*/});",
   			"    ~${1:${TM_FILENAME_BASE}}();",
   			"};",
   			"",
   			"#endif"
   		],
   		"description": "이 스니펫은 ifnde~endif를 작성하는 용도입니다."
   	},
```

- "setHPP" : 스니펫 이름이다. 만약 description이 설정되어있지 않으면 인텔리센스에 대신 display된다.

- "prefix": body 부분을 불러올 때 쓴다. 요걸 입력하는 식으로 snippet을 쓰게 될 것.

- "body": 불러오고 싶은 형태로 내용을 채워넣는다. vscode snippet 문법이 있는데, 유용한 것 두가지만 소개하자면~
  TM_FILENAME_BASE : 확장자를 떼어낸 파일이름을 가져온다. 42seoul cpp 프로젝트에서는 클래스마다 클래스이름.hpp, 클래스이름.cpp 파일을 하나씩 만들도록 하고 있으므로 엄청 요긴하다.
  $1{} $2{} $3{}...: 스니펫 body를 불러왔을 때 넘버링한 순서대로 블록지정 되어있어서 편하게 수정가능하도록 하고, tab으로 이동할 수 있게 한다.

- "description": prefix를 칠 때 인텔리센스에 display되는 설명이다.

![설명이랄까](https://user-images.githubusercontent.com/54612343/90474471-50630c80-e160-11ea-9920-b33d3a627fe4.gif)

기초적인 스니펫만으로도 위처럼 간편하게 작업할 수 있다.
위 예에 포함된 내용말고도 유용한 snippet body 문법이나 key binding 방법 등이 많다. 자세한 내용은 [Microsoft-Visual Studio Code's snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets) 링크에 너무나 자세하게 설명되어있으니 읽고 응용해보자.
