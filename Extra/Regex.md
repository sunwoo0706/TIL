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

### 문자 집합 (Character Set)

모든 문자를 나타낼 수 있는 '.' 과 달리, 대괄호([])를 사용하여 문자 집합을 표현할 수 있다.

<small>Regex</small>
```
f[ie]
```

<small>Text</small>
```
(fi)re
siren
(fe)male
(fi)nally
apple
airport
```

문자 집합은 한마디로 문자 집합 중 하나가 일치하는 경우를 의미한다고 생각하면 된다.

#### 문자 집합의 범위 (Range)

<small>Regex</small>
```
...[0123456789]
```

<small>Text</small>
```
abcd.txt
abce.txt
(abc0).txt
abcf.txt
(abc1).txt
(abc2).txt
(abc3).txt
```

매치된 문자열을 살펴보면, 아무 문자 3개 뒤에 숫자가 등장해야만 매치가 되는 것을 볼 수 있다. 하지만 저렇게 일일히 숫자를 다 쓰는것은 효율적이지 않기 때문에 regex에서는 하이픈(-) 을 제공한다.

<small>Regex</small>
```
...[0123456789]
```

<small>Regex</small>
```
...[0-9]
```

위 두 코드는 똑같은 동작을 하는 regex 코드이다. 또한 숫자가 아닌 문자에서도 [a-z]나 [A-Z] 같이 사용가능하다. (영어가 아니더라도 아스키 문자라면 무엇이든지 사용할 수 있다. Range의 범위 지정시 앞에는 작은 값이 나와야 한다.)
문자 범위 여러개를 [a-zA-Z0-9]와 같이 문자 집합 하나에 포함시킬 수 있다.

#### 문자열 집합 제외

특정 문자들을 제외하고 문자열을 검색하고 싶을때는 캐럿(^) 을 사용하면 된다.

<small>Regex</small>
```
...[^0-9]\.
```

<small>Regex</small>
```
(abcd.)txt
(abce.)txt
abc0.txt
(abcf.)txt
abc1.txt
abc2.txt
abc3.txt
```

#### 메타 문자

정규 표현식에서의 메타 문자는 이미 사전에 약속되어진 문자를 뜻합니다. 사전에 약속된 문자이기에, 메타 문자는 그대로 쓸 수 없으며 만약 문자로 쓰려면 역슬래시를 덧붙여 주어야 합니다.

| 메타 문자 | 설명 |
| :-: | :- |
| \v | 수직 탭 |
| \n | 개행 |
| \f | 폼 피드 |
| \r | 캐리지 리턴 |
| \t | 탭 |
| [\b] | 백스페이스 |
| \d | [0-9]와 동일한 기능 |
| \D | [^0-9]와 동일한 기능 |
| \w | [a-zA-Z0-9_]와 동일한 기능 |
| \W | [^a-zA-Z0-9_]와 동일한 기능 |
| \s| [\f\n\r\t\v]와 동일한 기능 |
| \S | [^\f\n\r\t\v]와 동일한 기능 |
| \x | 16진수 숫자와 일치 |
| \0 | 8진수 숫자와 일치 |