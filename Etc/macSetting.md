# 맥북 개발환경 세팅

## 1. homebrew 설치

---

- 왜 설치 하는가

> homebrew를 설치하는 이유는 Apple(또는 Linux 시스템)에서 제공하지 않는 유용한 패키지 관리자를 설치하기 위함이다.

---

- 설치 방법

1. [homebrew사이트](https://brew.sh/index_ko)를 들어간다.

<img src="./images/homebrew.png" align="center">

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<small>맥os에서 기본제공하는 터미널을 실행시키고 웹 코드를 복사, 붙여넣기한다.</small>

```bash
$ brew install [패키지명]
```
앞으로는 위 코드 형식처럼 패키지를 다운받는다.