# \<base>

**HTML** `<base>` 요소는 문서 안의 모든 상대 URL이 사용할 URL을 지정합니다. 문서에는 하나의 `<base>요소만 존재할 수 있습니다.

문서의 기준 URL을 스크립트에서 접근해야할 땐 `document.baseURI`을 사용할 수 있습니다. 문서에 `<base>`요소가 존재하지 않을 때 `baseURI`의 기본값은 `location.href`입니다.
