## Event

이벤트란 여러분이 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생을 뜻한다. 이는 여러분이 원한다면 사건이나 발생들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것이다.

### event target

target은 이벤트가 일어날 객체를 의미한다. 아래 코드에서 타겟은 버튼 태그에 대한 객체가 된다.

```html
<input type="button" onclick="alert(window.location)" value="alert(window.href)" />
```

### event type

이벤트의 종류를 의미한다. 위의 예제에서는 click이 이벤트 타입이다. 그 외에도 scroll은 사용자가 스크롤을 움직였다는 이벤트이고, mousemove는 마우스가 움직였을때 발생하는 이벤트이다.

이벤트의 종류는 이미 약속되어 있다. 여러가지 이벤트 종류를 보고 싶다면 [링크](https://developer.mozilla.org/en-US/docs/Web/Reference/Events)를 타고 들어가 봐보자

### event handler

이벤트가 발생했을 때 동작하는 코드를 의미한다. 위의 예제에서는 alert(windwo.location)이 여기에 해당한다.

### 이벤트 등록 방법

이벤트 등록 방법에는 3가지가 있다.

- inline 등록
- 프로퍼티 리스너
- addEventListener()

#### inline 등록

인라인 방식은 이벤트를 이벤트 대상의 태그 속성으로 지정하는 것이다. 다음은 버튼을 클릭했을 때 Hello world를 경고창으로 출력한다.

이벤트가 발생한 대상을 필요로하는 경우 this를 통해서 참조할 수 있다.

```html
<!--자기 자신을 참조하는 불편한 방법-->
<input type="button" id="target" onclick="alert('Hello world, '+document.getElementById('target').value);" value="button" />
<!--this를 통해서 간편하게 참조할 수 있다-->
<input type="button" onclick="alert('Hello world, '+this.value);" value="button" />
```

- 장점 : 태그에 이벤트가 포함되기 때문에 이벤트의 소재를 파악하는 것이 편리하다.
- 단점 : 방법 자체만으로 관심사의 분리를 부정한다. 그리고 이벤트 핸들러가 길 경우 코드 가독성이 떨어진다.

#### 프로퍼티 리스너

프로퍼티 리스너 방식은 이벤트 대상에 해당하는 객체에 프로퍼티로 이벤트를 등록하는 방식이다. 인라인 방식에 비하여 HTML과 JavaScript를 분리할 수 있다는 점에서 선호하는 방식이다.

이벤트가 발생한 대상을 필요로하는 경우 파라미터로 넘어온 이벤트객체에 target을 체이닝하여 사용할 수 있다.

```html
<body>
    <input type="button" id="target" value="button" />
<script>
    var t = document.getElementById('target');
    t.onclick = function(event){
        alert('Hello world, '+event.target.value)
    }
</script>
```

ie8 이하 버전에서는 이벤트 객체를 핸들러의 인자가 아니라 전역객체의 event 프로퍼티로 제공한다. 또한 target 프로퍼티ㅗ 지원하지 않는다. 아래는 이 문제를 해소하기 위한 코드다.

```html
<input type="button" id="target" value="button" />
<script>
    var t = document.getElementById('target');
    t.onclick = function(event){
        var event = event || window.event;
        var target = event.target || event.srcElement;
        alert('Hello world, '+target.value)
    }
</script>
```

장점 : 인라인 방식에 비하여 관심사의 분리가 가능하다
단점 : 이벤트 타입별로 오로지 하나의 이벤트 리스너만 등록이 가능하다.

#### addEventListner

addEventListener는 이벤트를 등록하는 가장 권장하는 방식이다. 이 방식을 이용하면 여러개의 이벤트 핸들러를 등록할 수 있다.

```html
<input type="button" id="target" value="button" />
<script>
    var t = document.getElementById('target');
    t.addEventListener('click', function(event){
        alert('Hello world, '+event.target.value);
    });
</script>
```

이 방식은 ie8 이하에서는 호환되지 않는다. ie에서는 attachEvent 메서드를 사용해야 한다.

```js
var t = document.getElementById('target');
if(t.addEventListener){
    t.addEventListener('click', function(event){
        alert('Hello world, '+event.target.value);
    }); 
} else if(t.attachEvent){
    t.attachEvent('onclick', function(event){
        alert('Hello world, '+event.target.value);
    })
}
```

이 방식의 중요한 장점은 하나의 이벤트 대상에 복수의 이벤트 타입 리스너를 등록할 수 있다는 점이다.

```html
<input type="button" id="target" value="button" />
<script>
    var t = document.getElementById('target');
    t.addEventListener('click', function(event){
        alert(1);
    });
    t.addEventListener('click', function(event){
        alert(2);
    });
</script>
```

이벤트 객체를 이용하면 복수의 엘리먼트에 하나의 리스너를 등록해서 재사용할 수 있다.

```html
<input type="button" id="target1" value="button1" />
<input type="button" id="target2" value="button2" />
<script>
    var t1 = document.getElementById('target1');
    var t2 = document.getElementById('target2');
    function btn_listener(event){
        switch(event.target.id){
            case 'target1':
                alert(1);
                break;
            case 'target2':
                alert(2);
                break;
        }
    }
    t1.addEventListener('click', btn_listener);
    t2.addEventListener('click', btn_listener);
</script>
```

장점 : 하나의 이벤트 대상에 복수의 이벤트 리스너를 등록가능하며 이벤트 리스너를 취소할 수 있다.
단점 : attachEvent()의 경우 this의 값이 이벤트가 바인드되어 있는 요소 대신에, window객체에 대한 참조가 된다.

### 메모리 이슈

```js
var i;
var els = document.getElementsByTagName('*');

// Case 1
for(i=0 ; i<els.length ; i++){
  els[i].addEventListener("click", function(e){/*do something*/}, false);
}
```

위의 경우 반복이 돌때마다 새로운 익명 핸들러 함수가 생성된다.
그에 반해 아래의 경우에는 이전에 선언한 동일한 함수를 이벤트 핸들러로 사용하므로, 메모리 소비가 줄어든다.

```js
// Case 2
function processEvent(e){
  /*do something*/
}

for(i=0 ; i<els.length ; i++){
  els[i].addEventListener("click", processEvent, false);
}
```

또한 첫번째 경우에는 `removeEventListener` 를 호출할 수 없다. 익명 함수에 대한 참조가 유지되지 않기 때문이다. (루프가 생성할 수 있는 여러개의 익명 함수 중 하나에 보관되지 않는다.) 두 번째 경우에는 processEvent가 함수 참조이기 때문에, myElement.removeEventListener("click", processEvent, false)를 수행할 수 있다.

사실, 메모리 소비와 관련하여, 함수 참조를 유지하는 것은 진짜 문제가 아니다. 오히려 정적 함수 참조를 유지하는 것이 부족할 뿐이다.

아래의 두 경우 모두 함수 참조가 유지되지만, 각 반복에서 재정의 되므로 정적이 아니다.

```js
// For illustration only: Note "MISTAKE" of [j] for [i] thus causing desired events to all attach to SAME element

// Case 3
for(var i=0, j=0 ; i<els.length ; i++){
  /*do lots of stuff with j*/
  els[j].addEventListener("click", processEvent = function(e){/*do something*/}, false);
}

// Case 4
for(var i=0, j=0 ; i<els.length ; i++){
  /*do lots of stuff with j*/
  function processEvent(e){/*do something*/};
  els[j].addEventListener("click", processEvent, false);
}
```

세 번째 경우에는 익명 함수에 대한 참조가, 반복될 때 마다 다시 할당된다. 네 번쨰 경우에는 전체 함수 정의가 변경되지 않지만, 새로운 것처럼 반복적으로 정의되고 있고 그래서 정적이지 않다. 따라서 간단하게 여러개의 동일한 이벤트 리스너인 것처럼 보이지만. 두 경우 모두 각 반복은 핸들러 함수에 대한 고유한 참조로 새로운 리스너를 생성한다. 그러나 함수 정의 자체는 변경되지 않으므로, 모든 중복 리스너에 대해 같은 함수가 여전히 호출될 수 있다.

또란 두 경우 모두 함수 참조가 우지되었지만, 각 가산에 대해 반복적으로 재정의 되었습니다. 위에서 사용했던 remove문으로는 리스너를 제거할 수 있지만, 마지막으로 추가한 리스너만 제거됩니다.
