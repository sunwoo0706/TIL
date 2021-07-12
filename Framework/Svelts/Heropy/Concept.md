### Svelts란?

Svelts는 [Rich Harris](https://twitter.com/rich_harris)가 제작한 프론트엔드 프레임워크입니다.
Svelts의 별명으로는 '프레임워크가 없는 프레임워크' 혹은 '컴파일러'이 있습니다.
이는 Virtual(가상) DOM이 없고, Runtime(런타임)에 로드할 프레임워크가 없음을 의미합니다.
기본적으로 빌드 단계에서 구성 요소를 컴파일하는 도구이므로 페이지에 단일 번들을 로드하여 앱을 렌더링할 수 있습니다.

최근까지 `'The magical disappearing UI framework'` 태그라인을 사용했습니다.
지금은 `'Cybernetically enhanced web apps'`라는 태그라인으로 변경되었습니다.

### 여타 프레임워크와의 차이점

1. 적은 양의 코드로 이루어져있음

- 높은 가독성 유지
- 개발 시간 단축
- 쉬운 리팩토링
- 쉬운 디버깅
- 더 작은 번들(SPA 최적화)
- 낮은 러닝 커브

2. 가상돔을 사용하지 않음

- 존나 빠름
- No diffing
- No overhead

> 내가 이해한걸로 치자면 런타임으로 계속 변경 사항을 기다리고 있는것이 아니라 빌드가 될때 이미 어떻게 변할지 한마디로 경우의수를 알고 있는것 같다.

3. Truly reactives

- Framework-less VanillaJS
- 오로지 'devDependcies'를 사용합니다.
- 명시적 설계(창의적 작업)

### 단점

- 낮은 성숙도
- CDN 미제공
- IE 지원??????????
