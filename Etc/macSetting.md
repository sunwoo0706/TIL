# 맥북 개발환경 세팅

## 1. homebrew 설치

---

- 왜 설치하는가

> homebrew를 설치하는 이유는 Apple(또는 Linux 시스템)에서 제공하지 않는 유용한 패키지 관리자를 설치하기 위함이다.

---

- 설치 방법

1. [homebrew사이트](https://brew.sh/index_ko)를 들어간다.

<img src="./images/homebrew.png" align="center">

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. 맥os에서 기본제공하는 터미널을 실행시키고 웹 코드를 복사, 붙여넣기한다.

---
- 사용 방법
```bash
$ brew install [패키지명]
```

---

## 2. iTerm2 설치

---

- 왜 설치하는가

> <b>Smart Selection</b><br />
Smart Selection은 regex에 매칭 되는 텍스트를 선택했을 때 발생되는 이벤트를 정의할 수 있습니다.

> <b>비쥬얼 비프</b>
시스템 비프가 짜증날때 이미지 형태로 비프를 보여줍니다.
<img src="./images/visual bell.gif" width="390" />

> 기타 등등

---

- 설치 방법

1. [iTerm2사이트](https://iterm2.com/)를 들어간다.

<img src="./images/iterm site.png" width="500"/>

2. 다운로드 버튼을 클릭한다.

3. .zip 파일을 열러 실행 시킨후 다운받아준다.

---

3. zsh 설치

---

- 왜 설치하는가

> zsh는 bash를 대신하는 shell 환경이다. oh-my-zsh까지 설치하면 CLI 사용이 아주 편리해 지기 때문이다.

---

- 설치 방법

1. zsh 설치
```bash
brew install zsh
```
2. zsh 설치 경로 확인
```bash
which zsh
```
2. 기본 shell로 변경
```bash
chsh -s $(which zsh)
```
- 만약 zsh접근이 잘 되지 않는다면
> 터미널 환경설정 `일반` -> `셀 열기`를 “기본 로글인 셀”에서 “명령어(절대경로)“로 바꾸고 `/usr/local/bin/zsh` (zsh 설치경로) 를 입력합니다. 혹은, `/etc/shells` 파일에 `/usr/local/bin/zsh` 를 추가합니다.

---

### oh-my-zsh 설치하기

---

- 왜 설치하는가

> zsh를 더 편리하게 사용할 수 있게 도와주는 프레임워크로, 플러그인과 테마를 편리하게 사용하기 위해서 필요합니다.

---

- 설치 방법

1. wget curl 설치
```bash
brew install curl
```
2. oh-my-zsh 설치
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

