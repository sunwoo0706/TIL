## Regex

> 정규 표현식 (Regular Expression)는 문자열을 검색하거나, 혹은 치환하거나 어떠한 문자열을 추출하고자 할때 주로 쓰인다.

### 간단한 문자열 찾기

#### Plain Text

문자열 그대로를 regex에 사용할 수 있다.

<small>Regex</small>
```
Text
```

<small>Text</small>
```
ABC(Text) (Text) | (Text)y
```

#### Any Chrater

plaintext가 아닌 모르는 문자까지 찾고 싶다면 '.' (Any Chracter) 을 사용하면 된다. ('.' 문자는 모든 문자 "하나"와 일치한다.)

<small>Regex</small>
```
h.s
```

<small>Text</small>
```
I was fifty years old to-day. Half a century (has) hurried by since I first lay in my mother's wondering arms. To be sure, I am not old; but I can no longer deceive myself into believing that I am still young. After all, the illusion of youth is a mental habit consciously encouraged to defy and face down the reality of age. If, at twenty, one feels that he (has) reached man's estate he, nevertheless, tests (his) strength and abilities, (his) early successes or failures, by the temporary and fictitious standards of youth.
```

'.' 문자 자체를 검색하고 싶다면, 역슬래시(\\)를 사용하면 된다.<br />
참고로 역슬래시 또한 '\\' 를 붙여서 사용하면 '\\' 문자 자체를 검색가능하다.
