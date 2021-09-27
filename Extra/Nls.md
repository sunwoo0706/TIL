## National Language Support

`microsoft/vscode` [📎](microsoft/vscode) 에 컨트리뷰팅하기 위하여 소스코드서핑을 하다가 `package.nls.json` [📎](https://github.com/microsoft/vscode/blob/main/extensions/json-language-features/package.nls.json) 라는 파일을 보게 되었습니다.

안에 내용은 다음과 같은 형식으로 이루어져 있었습니다.

```json
{
  "displayName": "Git",
  "description": "Git SCM Integration",

  ...

  "변수": "변수에 대한 설명"
}
```

nls가 무엇인지 궁금하여 구글링을 하게 되었고, 찾던중에 `National Language Support` 즉 연어현지화를 알게되었습니다.

언어현지화란 쉽게 말해서 여러분들이 게임을 할때 원어보다는 더빙이 이해하기 편하고, 책을 읽을때는 번역본이 읽기 편하듯 언어를 현지에 맞게 변형, 번역하여 이해하기 쉽게 하는것을 뜻합니다.

### 자세한 정의 [📎](https://ko.wikipedia.org/wiki/%EC%96%B8%EC%96%B4_%ED%98%84%EC%A7%80%ED%99%94)

> 언어 현지화(言語現地化)는 특정한 언어로 제작된 프로그램이나 제품을 다른 언어로 사용할 수 있게 하는 과정을 말한다. (번역 참조) 언어 패치는 그에 따른 패치를 말하며, 한국어로 사용할 수 있게 만들어 주는 패치를 흔히 한글 패치, 한글화 패치라고 부른다.

---

`microsoft/vscode` [📎](microsoft/vscode) 에서는 소스코드에서 쓰이고 있는 `variable` 들을 설명합니다. 즉 변수라는 **언어** 를 **현지화** 하기 때문에 `package.nls.json` [📎](https://github.com/microsoft/vscode/blob/main/extensions/json-language-features/package.nls.json) 로 작명했을거라 생각합니다.
