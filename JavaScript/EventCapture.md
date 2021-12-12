## Event Capture

이벤트 캡쳐는 [이벤트 버블링](./EventBubbling.md)과 반대 방향으로 진행되는 이벤트 전파 방식이다.

![이벤트 캡쳐 설명 사진](https://joshua1988.github.io/images/posts/web/javascript/event/event-capture.png)

위 그림처럼 특정 이벤트가 발생했을 때 최상위 요소인 body 태그에서 해당 태그를 찾아 내려간다. 그럼 이벤트 캡쳐는 코드로 어떻게 구현할 수 있을까.

```html
<body>
	<div class="one">
		<div class="two">
			<div class="three">
			</div>
		</div>
	</div>
</body>
```

```js
var divs = document.querySelectorAll('div');
divs.forEach(function(div) {
	div.addEventListener('click', logEvent, {
		capture: true // default 값은 false입니다.
	});
});

function logEvent(event) {
	console.log(event.currentTarget.className);
}
```

`addEventListener()` api에서 옵션 객체에 `capture: true` 를 설정해주면 됩니다. 그러면 해당 이벤트를 감지하기 위해 이벤트 버블링과 반대 방향으로 탐색한다.

따라서, 아까와 동일하게 `<div class="three"></div>` 를 클릭해도 아래와 같은 결과가 나타납니다.

![이벤트 캡쳐 결과 사진](https://joshua1988.github.io/images/posts/web/javascript/event/event-capture-log.png)