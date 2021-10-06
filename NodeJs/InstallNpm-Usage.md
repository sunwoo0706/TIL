### NPM

npm(Node Package Manager)은 Js및 세계 최대의 소프트웨어 레지스트리 패키지 관리자로 Node.js를 설치하면 같이 설치되어 사용할 수 있습니다.<br />
npm은 Node.js에서 사용되는 각종 코드 패키지들이 모여있고, 우리는 그 패키지를 다운로드 받아 사용할 수 있습니다.<br />
좀 더 쉽게 npm은 Node.js 생태계의 앱스토어나 플레이스토어 같은 역할을 합니다.

npm 레지스트리에는 640,000개가 넘는 패키지가 포함되어 있으며, 패키지는 의존성(depedencies) 및 버전을 추적할 수 있도록 구성됩니다<br />
이 페이지에서는 npm의 주요CLI(Command LIne Interface)와 관련된 정보들에 대해서 살펴보겠습니## init (초기화)

```bash
$ npm init
```

- package
- version
- description
- entry point
- test command
- git repositary
- keywords
- author
- license

여러 가지 질문에 답하면 (옵션을 추가하면) `package.json`파일을 작성합니다.<br />각 질문을 넘어가면 기본값을 사용합니다.

질문 없이 바로 시작하고 싶다면 `-f`(--force),`-y`(`--yes`)중 하나의 플래그를 추가하는 것을 추천합니다.

```bash
$ npm init -y
```

이미 `package.json`파일을 가지고 있다면, 먼저 그 파일을 읽고 난 후 옵션을 기본값을 사용합니다.

질문 없이 바로 시작하고 싶다면 `-f`(`--force`)`-y`(`--yes`)중 하나의 플래그를 추가하는 것을 추천합니다.

이미 `package.json`파일을 가지고 있다면, 먼저 그 파일을 읽고 난 후 옵션을 기본값으로 사용합니다.

### package.json

```json
{
  "name": "project-name",
  "version": "1.0.0",
  "keywords": [],
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Goolgae",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {}
}
```

`package.json`은 프로젝트 정보와 의존성(dependencies)을 관리하는 문서입니다.<br />
JSON 포맷으로 작성해야 하며, 다음과 같은 옵션들이 추가될 수 있습니다.

### name

URL이나 Command Line의 일부로 사용될 소문자로 표기된 214자 이내의 프로젝트(패키지) 이름으로, 간결하고 직관적인 이름으로 설정하되 다른 모듈과 동일한 이름은 피하세요.

### version

[SemVer(The semantic versioner for npm)](https://docs.npmjs.com/cli/v6/using-npm/semver)로 분석 가능한 형태의 버전을 지정합니다.

### description

프로젝트(패키지)의 설명을 지정합니다.<br />
(npm search 사용 시 도움이 됩니다.)

### keywords

프로젝트(패키지)의 키워드를 배열로 지정합니다.<br />
(npm search 사용 시 도움이 됩니다.)

```json
{
  "keywords:": ["array", "string"]
}
```

### homepage

프로젝트 홈페이지로 연결되는 URL을 지정합니다.

### bugs

패키지에 문제가 있을 때 보고될 트래커(추적시스템) 및 이메일 주소 등에 대한 URL을 지정합니다.

```json
{
  "bugs": {
    "url": "https://github.com/owner/project/issues",
    "email": "sunwoo0706@icloud.com"
  }
}
```

### license

패키지 사용을 허용하는 방법과 제한 사항을 알 수 있도록 라이센스를 지정합니다.
[Open Source License](https://opensource.org/licenses)

## author

제작자의 이름을 지정합니다.

## files

패키지가 의존성으로 설치될 때 같이 포함될 파일들의 배열입니다.<br />

```json
{
  "files": ["dist/", "js/{src,dist}/", "scss/"]
}
```

### main

프로그램의 기본 진입 점(entry point)를 지정합니다.<br />
패키지의 이름이 `jQuery`이고, 사용자가 `require('jQuery')`를 사용하면 진입 점의 메인 모듈에서 exports object가 반환(return)됩니다.

### repository

코드가 존재하는 장소를 지정합니다.<br />
Github을 사용하면 `npm docs`명령을 사용하여 찾을 수 있습니다.

```bash
{
  "repository": {
    "type": "git",
    "url": "https://github.com/npm/npm.git"
  }
}
```

### script

패키지 라이프 사이클에서 여러 번 실행되는 스크립트 명령을 포함합니다.

```json
  "scripts": {
    "lint": "bash lint.sh",
    "dev": "webpack-dev-server",
    "prod": "webpack -p"
  }
}
```

### dependencies

패키지의 배포 시 포함될 의존성 모듈을 지정합니다.

### devDependencies

패키지의 호환성 모듈을 지정합니다.<br />
(npm@3 이후로 배포 시 포함되지 않습니다.)

### peerDependencies

패키지의 호환성 모듈을 지정합니다.<br />
(npm@3 이후로 배포 시 포함되지 않습니다, 대신 호환성 모듈이 없으면 경고 메세지가 표시됩니다.)

```bash
{
  "name": "bootstrap",
  "peerDependencies": {
    "jquery": "1.9.1 - 3",
    "popper.js": "^1.12.9"
  }
}
```

### bundledDependencies

패키지를 게시할 때 번들로 묶을 패키지의 이름을 **배열**로 지정합니다.<br />
npm 패키지를 로컬에서 보존해야 하거나 단일 파일 다운로드를 통해 사용할 수 있는 경우 `npm pack`을 실행하여 패키지를 `<name>-<version>.tgz`형태의 [tarball](<https://ko.wikipedia.org/wiki/Tar_(%ED%8C%8C%EC%9D%BC_%ED%8F%AC%EB%A7%B7)>)파일로 묶을 수 있습니다.

```bash
{
  "bundledDependencies": [
    "renderized",
    "super-streams"
  ]
}
```

### optionalDependcies

npm을 찾을 수 없거나 설치에 실패한 경우 계속 진행하려면 optionDependencies 객체에 넣을 수 있습니다.<br />
depenedcies 동일하게 배포 시 포함될 의존성 모듈을 지정하지만, 빌드 실패로 인해 설치 과정이 중단되지 않습니다.

```bash
{
  "optionalDependencies": {
    "7zip-bin-mac": "^1.x.x",
    "7zip-bin-win": "^2.x.x"
  }
}
```

### engines

패키지가 작동하는 Node 버전을 지정합니다.

```bash
{
  "engines": {
    "node": ">=0.10.3 <0.12",
    "npm" : "~1.0.20"
  }
}
```

### private

개인 저장소의 우연한 발행을 방지하기 위해 npm에서 패키지의 공개 여부를 지정합니다.

```bash
{
  "private": true
}
```

### paskage-lock.json

`package.json`이 동일한 개발 환경 구축을 위한 정보를 가지고 있지만, 다양한 경우에 의해 동일한 개발 환경 구축에 문제가 발생할 수 있습니다.

예들 들어, 다음과 같은 어떤 상위(`dashdash`)에서 사용하는 하위 모듈 중 하나(`assert-plus`)`의 버전이 변경되었다고 가정합니다.<br />
그렇다면 상위 모듈 버전이 동일하다가 하더라도 내부적으로 다른 결과를 출력할 수 있습니다.

```bash

```
