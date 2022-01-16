## --target_arch

한마디로 다른 OS/아키텍쳐용 패키지를 다운로드할 수 있도록 지시하는 옵션이다. 

이상하게도 `npm` 문서 어디에도 작성되어있지않아서 관련된 내용을 계속 찾다가,
대부분의 `node_modules` 는 OS/arch/v8 ABI(컴파일된 API라고 생각하면 될 듯) 조합에 대해 설치 스크립트로 `node-pre-gyp` 를 사용한다. 하나라도 사용할 수 없는 경우 기본 빌드로 대체한다는 사실을 알게 되었다.

그러니 `node_modules` 가 `node-pre-gyp`를 사용한다고 가정할때 다른 OS/아키텍쳐용 패키지를 다운로드하고 싶을때 다음과 같이 사용 가능하다.

```sh
npm i --target_arch=x64 --target_platform=linux
```

platform은 운영체제를 의미한다.