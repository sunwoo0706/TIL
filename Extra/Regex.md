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

#### 역참조 (backreferences)

말 그대로 역으로 참조하는 것을 나타냅니다. 정규 표현식에서는 패턴의 일부를 하위 표현식으로 묶으면, 첫번째로 나타나는 부분 문자열을 버퍼에 저장하고 따라오는 문자열에서 인덱스를 사용하여 버퍼에 저장된 문자열과 같은 문자열을 역참조 할 수 있다.

<small>Regex</small>

```
\b([a-z]+) \1\b
```

<small>Text</small>

```
why (so so) serious
```

위의 정규표현식을 자세히 살펴보면, \b라는 메타 문자가 사용되었다. 이 \b는 단어의 경계를 구분짓는 메타 문자로, 여기 텍스트에선 공백이 단어와 단어를 구분짓는 문자이므로 공백은 \b와 같다.

위에 예시에서는 [a-z]+를 하위 표현식으로 묶었다. 이렇게 묶은 하위 표현식은 임시 버퍼에 저장되고, 이 임시 버퍼에 접근하려면 \n 을 통해 각 버퍼에 접근할 수 있습니다. 여기서 n은 개행 문자가 아니라 n은 1이상 99이하의 인덱스 번호이다. 이런 역참조를 통해, 반복되는 문자를 쉽게 찾을 수 있다. 참고로, 두자리 이상이 넘어가는 숫자에 해당하는 역참조가 존재하고 해당 그룹 숫자에 해당하는 그룹이 있을 경우 역참조로 간주되나, 아닐 경우에는 구문 분석 오류로 간주된다.

#### 전방 탐색 (lookahead)

전방 탐색이란 작성한 패턴에 일치하는 영역이 존재햐여도 그 값이 제외되어서 나오는 패턴입니다. 전방 탐색 기호는 ?= 이며, = 다음에 오는 문자가 일치하는 영역에서 제외됩니다.

<small>Regex</small>

```
.+(?=:)
```

<small>Text</small>

```
(http)://www.abc.com
(https)://www.abc.com
(http)://www.abc.net
```

위에 쓰인 정규 표현식을 살펴보자면, 아무 문자가 한번 이상 연속적으로 등장하고 콜론 문자가 등장하는 문자열 중에서, 콜론 문자는 일치하는 영역에서 제외된다. 만약, 전방 탐색 기호를 쓰지 않고 콜론을 그대로 썼었다면, 콜론이 일치되는 영역에서 제외되지 않고 포함되어 버린다.

#### 후방 탐색 (lookbehind)

후방 탐색은 뒤에 있는 문자열을 탐색한다. 후방 탐색의 기호는 ?<=이다. 전방 탐색 기호의 ?와 = 사이에 < 기호가 추가된 것이다. 후방 탐색도, 전방 탐색의 사용법과 똑같다.

<small>Regex</small>

```
(?<=\$)[0-9.]+
```

<small>Text</small>

```
1: $(600.4)
2: $(10.25)
3: $(47.33)
4: $(112.34)
```

위에 쓰인 정규 표현식을 살펴보니, 후방 탐색 기호 뒤에 메타 문자인 \$ 가 쓰였다. 그렇기에, \로 이스케이프 해주어야한다.
그 후에, 숫자와 점으로 구성된 문자 집합이 연속된 문자열을 탐색한다. 일치된 텍스트를 살펴보면, \$ 기호 뒤에있는 문자들만 일치했음을 확인할 수 있다.

> 참고로, 전방 탐색과 후방 탐색은 너비가 0이며, 역참조가 불가능 하다.

너비가 0이라는 말이 정규표현식을 배우면서 조금씩 나오게되는 표현일텐데 본인은 검색문자열에서 차지하는 부분이 0이다라고 이해했다.

#### 부정형 전후방탐색 (negative lookaround)

이번에는 "부정형" 전후방탐색이라는 것에 주의를 기울여야 한다. 전에 보았던 탐색 기호들은 모두 "긍정형" 탐색이었다.
밑에 표를 봐보자.

| 탐색 기호 | 설명            |
| --------- | --------------- |
| (?=)      | 긍정형 전방탐색 |
| (?!)      | 부정형 후방탐색 |
| (?<=)     | 긍정형 전방탐색 |
| (?<!)     | 부정형 후방탐색 |

위의 표에서 부정형 탐색 기호에 ! 문자가 들어갔음을 확인할 수 있다. 긍정형 전후방탐색이 = 뒤 혹은 앞에 있는 문자와 일치하는 텍스트를 탐색하는 것이라면, 부정형 전후방탐색은 일치하지 않는 텍스트를 탐색하는 것이다.

<small>Regex</small>

```
\b(?<!\$)\d+
```

<small>Text</small>

```
$10 (5) $6 (77) $788
```

위에 쓰인 정규 표현식을 살펴보면, 단어 경계(\b)와 부정형 후방탐색(?<!)이 쓰였고, 부정형 후방탐색 기호 뒤에 $ 문자가 등장했다. 그 후에는 연속된 숫자(\d+)를 의미하므로 \$ 뒤에 숫자가 들어간 영역은 제외하겠다는 소리다. \$ 가 안들어가고 숫자만 달랑 있는 영역만 탐색하는 것이다. 단어 경계만 설명을 보충하자면, 단어와 단어를 구분짓는 경계이다. 여기서는 공백이 단어와 단어를 구분짓는 경계인 셈이다.
