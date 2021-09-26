## Yarn Berry

### 개요

**Yarn Berry 란?**

Yarn Berry는 Node.js를 위한 새로운 패키지 관리 시스템으로, yarn v1의 주요 개발자인 [Maël Nison](https://github.com/arcanis/) 씨가

만들었습니다. 2020년 1월 25일부터 정식 버전(v2)가 출시되어, 현재는 Babel과 같은 큰 오픈소스 레포지터리에서도 채택하고 있습니다.

[yarnpkg/berry](https://github.com/yarnpkg/berry) 레포지터리에서 소스코드가 관리되고 있습니다.

Yarn Berry는 기존의 "깨져 있는" NPM 패키지 관리 시스템을 혁신적으로 개선합니다.

**NPM의 문제점**

NPM은 Node.js 설치 시에 기본으로 제공되어 범용적으로 사용되고 있으나, 비효율적이거나 깨져 있는 부분이 많습니다.

![img1](https://static.toss.im/assets/toss-tech/yarn-berry-1.png)

**비효율적인 의존성 검색**

NPM은 파일 시스템을 이용하여 의존성을 관리합니다. 익숙한 `node_modules` 폴더를 이용하는 것이 특징인데요. 이렇게 관리했을 때 의존성 검색은 비효율적으로 동작합니다.

예를 들어, `/Users/toss/dev/toss-frontend-libraries` 폴더에서 `require()` 문을 이용하여 `react` 패키지를 불러오는 상황을 가정합시다.

라이브러리를 찾기 위해 순회하는 디렉토리의 목록을 확인하려고 할 때, Node.js에서 제공하는 `require.resolve.paths()` 함수를 사용할 수 있습니다. 이 함수는 NPM이 검색하는 디렉토리의 목록을 반환합니다.

```sh
$ node
Welcome to Node.js v12.16.3.
Type ".help" for more information.
> require.resolve.paths('react')
[
  '/Users/toss/dev/toss-frontend-libraries/repl/node_modules',
  '/Users/toss/dev/toss-frontend-libraries/node_modules',
  '/Users/toss/node_modules',
  '/Users/node_modules',
  '/node_modules',
  '/Users/toss/.node_modules',
  '/Users/toss/.node_libraries',
  '/Users/toss/.nvm/versions/node/v12.16.3/lib/node',
  '/Users/toss/.node_modules',
  '/Users/toss/.node_libraries',
  '/Users/toss/.nvm/versions/node/v12.16.3/lib/node'
]
```

목록에서 확인할 수 있는 것처럼, NPM은 패키지를 찾기 위해서 계속 상위 디럭토리의 node_modules 폴더를 탐색합니다. 따라서 패키지를 바로 찾지 못할수록 readdir, stat과 같은 느린 I/O 호출이 반복됩니다. 경우에 따라서는 I/O 호출이 중간에 실패하기도 합니다.

TypeScript 4.0까지는 node_modules를 이용한 패키지 탐색이 너무 비효율적인 나머지, 패키지를 처음으로 import 하기 전까지는 node_modules 내부의 타입 정보를 찾아보지 않기도 했습니다.

**환경에 따라 달라지는 동작**

NPM은 패키지를 찾지 못하면 사위 디렉토리의 node_modules 폴더를 계속 검색합니다. 이 특성 때문에 어떤 의존성을 찾을 수 있는지는 해당 패키지의 상위 디렉토리 환경에 따라 달라집니다.

예를 들어, 상위 디렉토리가 어떤 node_modules를 포함하고 있는지에 따라 의존성을 불러올 수 있기도 하고, 없기도 합니다. 다른 버전의 의존성을 불러올 수 있는 여지도 존재합니다.

이렇게 환경에 따라 동작이 변하는 것은 나쁜 징조입니다. 해당 상황을 재현하기 까다로워지기 때문입니다.

**비효율적인 설치**

NPM에서 구성하는 node_modules 디렉토리 구조는 매우 큰 공간을 차지합니다. 일반적으로 간단한 CLI 프로젝트도 수백 메가바이트의 node_modules 폴더가 필요합니다. 용량만 많이 차지할 뿐 아니라, 큰 node_modules 디렉토리 구조를 만들기 위해서는 많은 I/O 작업이 필요합니다.

Node_modules 폴더는 복잡하기 때문에 설치가 유효한지 검증하기 어렵습니다. 예를 들어, 수백 개의 패키지가 서로를 의존하는 복잡한 의존성 트리에서 node_modules 디렉토리 구조는 깊어집니다.

이렇게 깊은 트리 구조에서 의존성이 잘 설치되어 있는지 검증하려면 많은 수의 I/O 호출이 필요합니다. 일반적으로 디스크 I/O 호출은 메모리의 자료구조를 다루는 것보다 훨씬 느립니다. 이런 문제로 인해 Yarn v1이나 NPM은 기본적인 의존성 트리의 유효성까지만 검증하고, 각 패키지의 내용이 올바른지는 확인하지 않습니다.

**유령 의존성**

NPM 및 Yarn v1에서는 중복해서 설치되는 node_modules를 아끼기 위해 끌어올리기(Hoisting) 기법을 사용합니다.

![img2](https://static.toss.im/assets/toss-tech/yarn-berry-2.png)

예를 들어, 의존성 트리가 왼쪽의 모습을 하고 있다고 가정합시다.

왼쪽 트리에서 **[A (1.0)]**과 **[B (1.0)]** 패키지는 두 번 설치되므로 디스크 공간을 낭비합니다. NPM과 Yarn v1에서는 디스크 공간을 아끼기 위해 원래 트리의 모양을 오른쪽 트리처럼 바꿉니다.

오른쪽 트리로 의존성 트리가 바뀌면서 package-1 에서는 원래 require() 할 수 없었던 **[B (1.0)]** 라이브러리를 불러올 수 있게 되었습니다.

이렇게 끌어올리기에 따라 직접 의존하고 있지 않은 라이브러리를 require() 할 수 있는 현상을 유령 의존성(Phantom Dependency)이라고 부릅니다.

유령 의존성 현상이 발생할 때, package.json에 명시하지 않은 라이브러리를 조용히 사용할 수 있게 됩니다. 다른 의존성을 package.json 에서 제거했을 때 소리없이 같이 사라지기도 합니다. 이런 특성은 의존성 관리 시스템을 혼란스럽게 만듭니다.

**Plug’n’Play (PnP)**

Yarn Berry는 위에서 언급한 문제를 새로운 Plug’n’Play 전략을 이용하여 해결합니다.

**Plug’n’Play의 배경**

Yarn v1은 package.json 파일을 기반으로 의존성 트리를 생성하고, 디스크에 node_modules 디렉토리 구조를 만듭니다. 이미 패키지의 의존성 구조를 완전히 알고 있는 것입니다.

node_modules 파일 시스템을 이용한 의존성 관리는 깨지기 쉽습니다. 모든 패키지 매니저가 실수하기 쉬운 Node 내장 의존성 관리 시스템을 사용해야 할까요? 패키지 매니저들이 node_modules 디렉토리 구조를 만드는 것에 그치지 않고, 보다 근본적으로 안전하게 의존성을 관리하면 어떨까요?

Plug’n’Play는 이런 생각에서 출발했습니다.

**ZipFS (Zip Filesystem)**

Yarn PnP 시스템에서 각 의존성은 Zip 아카이브로 관리됩니다. 예를 들어, Recoil 0.1.2 버전은 `recoil-npm-0.1.2-9a0edbd2b9-c69105dd7d.zip`과 같은 압축 파일로 관리됩니다.

이후 .pnp.cjs 파일이 지정하는 바에 따라 동적으로 Zip 아카이브의 내용이 참조됩니다.

Zip 아카이브로 의존성을 관리하면 다음과 같은 장점이 생깁니다.

1. 더 이상 node_modules 디렉토리 구조를 생성할 필요가 없기 때문에 설치가 신속히 완료됩니다.
2. 각 패키지는 버전마다 하나의 Zip 아카이브만을 가지기 때문에 중복해서 설치되지 않습니다. 각 Zip 아카이브가 압축되어 있음을 고려할 때, 스토리지 용량을 크게 아낄 수 있습니다.
3. 의존성을 구성하는 파일의 수가 많지 않으므로, 변경 사항을 감지하거나 전체 의존성을 삭제하는 작업이 빠릅니다.
