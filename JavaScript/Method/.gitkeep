## Test

한마디로 주어진 문자열이 정규 표현식을 만족하는지 판별하고, 그 여부를 boolean 값으로 반환한다.

```js
const str = 'table football';

const regex = new RegExp('foo*');
const globalRegex = new RegExp('foo*', 'g');

console.log(regex.test(str));
// expected output: true

console.log(globalRegex.lastIndex);
// expected output: 0

console.log(globalRegex.test(str));
// expected output: true

console.log(globalRegex.lastIndex);
// expected output: 9

console.log(globalRegex.test(str));
// expected output: false
```

### Syntax

> regexObject.test(str);

여기서 str은 정규 표현식 일치를 수행할 문자열을 뜻한다.