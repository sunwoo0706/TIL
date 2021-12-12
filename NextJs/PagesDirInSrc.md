## src/ 하위에 pages 디렉토리 넣기

루트 페이지 디렉토리의 대안으로 `src/` 아래에 `pages/` 디렉토리를 위치 시킬수 있다.

`src/`는 CRA에서도 사용하는 방식이며, 기본적으로 Next에서도 지원해준다.

### 주의 사항

`pages/` 가 루트 디렉토리에 있으면 `src/pages` 는 무시된다.

`next.config.js` 및 `tsconfig.json`과 같은 구성 파일은 루트 디렉터리 안에 있어야 하며 `src/`로 이동하면 작동하지 않습니다. `public/`도 마찬가지이다.
