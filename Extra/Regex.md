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

<small>Text</small>

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

| 메타 문자 | 설명                        |
| :-------: | :-------------------------- |
|    \v     | 수직 탭                     |
|    \n     | 개행                        |
|    \f     | 폼 피드                     |
|    \r     | 캐리지 리턴                 |
|    \t     | 탭                          |
|   [\b]    | 백스페이스                  |
|    \d     | [0-9]와 동일한 기능         |
|    \D     | [^0-9]와 동일한 기능        |
|    \w     | [a-zA-Z0-9_]와 동일한 기능  |
|    \W     | [^a-za-z0-9_]와 동일한 기능 |
|    \s     | [\f\n\r\t\v]와 동일한 기능  |
|    \S     | [^\f\n\r\t\v]와 동일한 기능 |
|    \x     | 16진수 숫자와 일치          |
|    \0     | 8진수 숫자와 일치           |

#### 연속된 문자 찾기

연속된 문자를 찾고 싶을때는 '+' 란 메타 문자를 사용할 수 있다.

<small>Regex</small>

```
\w+@\w+\.\w+
```

<small>Text</small>

```
(id@gmail.com)
id@daumnet
(id@naver.com)
(id@nate.com)
id@google
```

'+' 문자는 문자가 하나 이상 일치해야만 하는데 문자가 아예 없거나 하나 이상일 경우에는 '\*' 문자를 문자 또는 문자 집합 뒤에 써주면 된다.

<small>Regex</small>

```
bo+
```

<small>Text</small>

```
b
(bo)
(boo)
```

<small>Regex</small>

```
bo*
```

<small>Text</small>

```
(b)
(bo)
(boo)
```

문자가 없거나, 하나만 있으면 일치하게 하고 싶은 경우에는 '?'를 사용하면 된다.

<small>Regex</small>

```
aabb?cc
```

<small>Text</small>

```
(aabcc)
(aabbcc)
aabbbbcc
```

#### 수량자 (Quantifier)

| 수량자 | 설명                                |
| :----: | :---------------------------------- |
|  {n}   | n개만을 찾는다.                     |
|  {n,}  | n개 이상을 찾는다.                  |
| {n, m} | 최소 n개, 최대 m개의 경우를 찾는다. |

<small>Regex</small>

```
[0-9]{3}
```

<small>Text</small>

```
12
(123)
(123)4
(456)
(456)7
(456)78
```

<small>Regex</small>

```
[0-9]{3,}
```

<small>Text</small>

```
12
(123)
(1234)
(456)
(4567)
(45678)
```

<small>Regex</small>

```
[0-9]{3,4}
```

<small>Text</small>

```
12
(123)
(1234)
(456)
(4567)
(4567)8
```

#### 탐욕적 수량자와 게으른 수량자

+와 _ 그리고 {n,}은 탐욕적 수량자에 속한다. 왜 이렇게 불리우냐 하면 가능한 가장 큰 덩어리를 찾으려 하기 때문이다. 반면에 게으른 수량자는 가능한 가장 적은, 최소의 덩어리를 찾는다.+, _, {n,}은 탐욕적 수량자지만, 뒤에 ? 문자를 덧붙이면 게으른 수량자(+?, \*?, {n,}?)가 된다. 예시를 보는게 쉽다.

<small>Regex</small>

```
<b>.*</b>
```

<small>Text</small>

```
(<b>BOLD!</b><hr><b>BOLD!</b>)
```

<small>Regex</small>

```
<b>.*?</b>
```

<small>Text</small>

```
(<b>BOLD!</b>)<hr>(<b>BOLD!</b>)
```

탐욕적 수량자와는 달리 최소의 문자 덩어리만 일치하는게 게으른 수량자이다.

#### 하위 표현식 (Subexpression)

하위 표현식이란, 특정 패턴, 표현식을 하나의 항목으로 처리하는 것을 말한다. 이 하위 표현식을 사용하려면 소괄호를 사용해야 한다. 소괄호 역시 메타 문자이기 때문에, 소괄호 그 자체를 찾으려면 '\\'로 이스케이프 해줘야 한다.

<small>Regex</small>

```
(abcc)
abcabc
```

<small>Text</small>

```
(<b>BOLD!</b><hr><b>BOLD!</b>)
```

<small>Regex</small>

```
(abc){2}
```

<small>Text</small>

```
abcc
(abcabc)
```

위에 쓰인 정규 표현식에서 (abc)는 하위 표현식이다. 하위 표현식으로 사용되었기에, abc는 하나의 항목으로 처리된다.

#### 하위 표현식의 중첩

하위 표현식의 중첩이란 말 그대로 표현식의 자식으로 표현식을 둘 수 있다는 얘기다.

#### OR 연산자

둘 중 하나라도 일치할 경우를 생각해서 OR 연산자 '|'를 사용할 수 있다.

<small>Regex</small>

```
a|b
```

<small>Text</small>

```
(a)(b)
(a)
(a)|(b)
```
