## 이벤트 위임

> [이벤트 버블링](./EventBubbling.md)과 [캡쳐](EventCapture.md)는 이벤트 위임을 위한 선수 지식이라고 해도 과언이 아니다. 이벤트 위임은 실제 바닐라 js로 웹 앱을 구현할 때 자주 사용하게 되는 코딩 패턴이다.

이벤트 위임은 한마디로 **'하위 요소에 각각 이벤트를 붙이지 않고 상위 요소에서 하위 요소의 이벤트들을 제어하는 방식'** 이다.

백문이 불여일코, 아래 코드를 보자

```html
<h1>오늘의 할 일</h1>
<ul class="itemList">
	<li>
		<input type="checkbox" id="item1">
		<label for="item1">이벤트 버블링 학습</label>
	</li>
	<li>
		<input type="checkbox" id="item2">
		<label for="item2">이벤트 캡쳐 학습</label>
	</li>
</ul>
```

```js
var inputs = document.querySelectorAll('input');
inputs.forEach(function(input) {
	input.addEventListener('click', function(event) {
		alert('clicked');
	});
});
```

위 코드는 할 일 목록을 간단한 리스트 아이템으로 나타낸 코드이다.

여기서 할 일이 늘어나 리스트 아이템을 추가하면 어떻게 될까?

```js
var itemList = document.querySelector('.itemList');

var li = document.createElement('li');
var input = document.createElement('input');
var label = document.createElement('label');
var labelText = document.createTextNode('이벤트 위임 학습');

input.setAttribute('type', 'checkbox');
input.setAttribute('id', 'item3');
label.setAttribute('for', 'item3');
label.appendChild(labelText);
li.appendChild(input);
li.appendChild(label);
itemList.appendChild(li);
```

위 코드는 동작하지 않을것이다. 왜일까?

코드를 다시 살펴보면, 인풋 박스에 클릭 이벤트 리스너를 추가하는 시점에서 리스트 아이템은 두개이다.

따라서, 새롭게 추가된 리스트 아이템에는 클릭 이벤트 리스너가 등록되지 않은것이다.

이런식으로 매번 새롭게 추가된 리스트 아이템까지 클릭 이벤트 리스너를 일일이 달아줘야 할까?

리스트 아이템이 많아지면 많아질수록 이벤트 리스너를 다는 작업 자체가 매우 번거롭다. 이 번거로운 작업을 해결할 수 있는 방법이 바로 이벤트 위임이다.

앞에서 살펴본 코드를 아래와 같이 변경해보자

```js
// var inputs = document.querySelectorAll('input');
// inputs.forEach(function(input) {
// 	input.addEventListener('click', function() {
// 		alert('clicked');
// 	});
// });

var itemList = document.querySelector('.itemList');
itemList.addEventListener('click', function(event) {
    const input = event.target.closest('input');
    if ( ! input ) return;
	alert('clicked');
});

// 새 리스트 아이템을 추가하는 코드
// ...
```

화면의 모든 인풋 박스에 일일이 이벤트 리스너를 추가하는 대신 이제는 인풋 박스의 상위 요소인 ul태그, `.itemList`에 이벤트 리스너를 달아놓고 하위에서 발생한 클릭 이벤트를 감지한다.

이 부분이 [이벤트 버블링](./EventBubbling.md)이다.