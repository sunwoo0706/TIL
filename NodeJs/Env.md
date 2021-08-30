## env란?

먼저 환경 변수`(environment Variables)`가 무엇인지 간단하게 개념부터 짚고 넘어가겠습니다.

일반적으로 우리는 코드 베이스는 하나만 관리하고, 개발, 테스트, 운영 등 여러 환경에 애플리케이션을 배포하는데요. 어느 환경에 배포하느냐에 따라서 다르게 설정해야하는 항목은 보통 운영 체제 레벨에서 환경 변수를 통해 관리하게 됩니다.

대표적인 예로, 개발 환경에서는 로컬 DB를 사용해야하는데, 운영 환경에서는 원격 DB를 사용해야하는 경우를 들 수 있습니다. 뿐만 아니라 `DB password`나 `API key`와 같은 인증 정보는 공개된 코드 저장소에 올리면 안 되기 때문에 환경 변수로 저장해놓고 사용하는 것이 일반적입니다.

### 환경 변수 접근

Node.js에서 환경 변수에 접근할 때는 `process.env`라는 내장 자바스크립트 객체를 사용합니다. `process`는 _전역 객체여서 별도로 임포트해야하는 모듈이 없으며 애플리케이션 어디에서든지 접근이 가능합니다_.

따라서, Node.js 인터프리터를 실행하셔서 사용하시는 운영 체제의 어떤 환경 변수들이 설정되어 있는지 바로 확인해볼 수 있습니다.

```sh
$ node
Welcome to Node.js v14.15.0.
Type ".help" for more information.
> process.env.USER
'dale'
> process.env.HOME
'/Users/dale'
> process.env.LANG
'en_US.UTF-8'
> process.env.API_KEY
undefined
```

### 환경 변수 설정

환경 변수는 운영 체제에 따라서 다양한 방법으로 설정할 수 있는데요.

애플리케이션을 실행할 때 1회성으로 환경 변수를 설정하고 싶다면 node 명령어 앞에 환경 변수를 키=값 형태로 명시를 해줍니다.

```sh
$ API_KEY=abc DB_PASSWORD=1234 node
Welcome to Node.js v14.15.0.
Type ".help" for more information.
> process.env.API_KEY
'abc'
> process.env.DB_PASSWORD
'1234'
```

이렇게 Node.js 프로세스 레벨에서 설정해준 환경 변수는 해당 프로세스가 살아있는 동안에만 유효하며 프로세스를 종료하면 사라집니다. 따라서 다음과 같이 다시 Node.js 인터프리터를 실행하면 이 전에 실행할 때 명시했던 환경 변수를 얻을 수 없습니다.

운영 체제에서 지원하는 커맨드를 이용하면 설정한 환경 변수를 터미널 창을 닫을 때까지 유지할 수 있습니다. Node.js로 애플리케이션을 실행하기 전에 리눅스나 `Mac OS`에서는 `export 키=값`, `Windows` 에서는 `SET 키=값`를 이용해서 환경 변수를 설정해주면 됩니다.

```sh
$ export API_KEY=abc
$ export DB_PASSWORD=1234
$ node
Welcome to Node.js v14.15.0.
Type ".help" for more information.
> process.env.API_KEY
'abc'
> process.env.DB_PASSWORD
'1234'
```

`process.env`는 가변 객체이기 때문에 프로그램 내에서 얼마든지 새로운 항목을 설정하거나 기존에 설정된 값을 자유롭게 갱신 또는 제거할 수 있습니다.

```sh
$ node
Welcome to Node.js v14.15.0.
Type ".help" for more information.
> process.env.API_KEY = "abc"
'abc'
> process.env.API_KEY
'abc'
> process.env.API_KEY = "def"
'def'
> process.env.API_KEY
'def'
'1234'
> delete process.env.API_KEY
true
> process.env.API_KEY
undefined
```
