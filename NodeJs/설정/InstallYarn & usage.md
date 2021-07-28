# Yarn 설치 및 사용법

FaceBook에서 만든 자바스크립트 패키지 매니저인 Yarn을 사용해 봅시다.

## Yarn 설치

Yarn은 다양한 OS의 설치를 지원합니다.

## MacOS

[Homebrew](.../Etc/OsxSetting/macSetting.md)를 사용하는 설치

```bash
$ brew install yarn
```

NVM 같은 버전 관리 툴을 사용해야 한다면 Node.js의 설치를 제외하여야 합니다. (충도리 일어나거덩요.)

```bash
$ brew install yarn --without-node
```

## Windows

Chocolatey를 사용하여 설치하세요.<br />
(제가 윈도우를 안써서 설명은 길게 하지 않겠습니다.)

```bash
$ choco install yarn
```

Scoop도 사용해도됨<br />
(이것도 마찬가지로 설명 안해드림 알아서 구글링 ㄱ)

## NPM

NPM으로 설치할 수도 있습니다.<br />
(저는 이 방법을 선택했습니다.)

```bash
$ npm install -g yarn
```

<small>설치가 잘 되었는지 확인합니다.</small>

```bash
yarn --version
```

설치 후 전역 사용에 문제가 있다면 Path 설저을 해줘야 합니다.
```bash
$ export PATH="$PATH:/opt/yarn-[version]/bin"
```