## 이벤트 버블링

이벤트 버블링은 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성을 의미한다. 아래 그림을 보자.

![이벤트 버블링 설명 사진](https://joshua1988.github.io/images/posts/web/javascript/event/event-bubble.png)

> HTML 요소는 기본적으로 트리 구조를 갖습니다. 여기서는 트리 구조상으로 한 단계 위애 있는 요소를 상위 요소라고 하며 body 태그를 최상위 요소라고 부르겠다.

위 그림은 아래에 예시로 들 코드를 미리 도식화한 그림이다. 세 개의 div 태그가 있고 가장 아래에 있는 div 태그에서 이벤트가 발생했을 때 최상위 요소인 body 태그까지 이벤트가 전달되는 모습을 나타내었다. 그럼 코드를 봐보자

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
	div.addEventListener('click', logEvent);
});

function logEvent(event) {
	console.log(event.currentTarget.className);
}
```

위 코드는 세 개의 div 태그에 모두 클릭 이벤트를 등록하고 클릭 했을 때 logEvent 함수를 실행시키는 코드이다. 여기서 위 그림대로 최하위 div 태그 `<div class="three"></div>` 를 클릭하면 아래와 같은 결과가 실행된다

![이벤트 버블링 사진](https://joshua1988.github.io/images/posts/web/javascript/event/event-bubble-log.png)

div 태그 한 개만 클릭했을 뿐인데 왜 3개의 이벤트가 발생되는 것일까? 그 이유는 브라우저가 이벤트를 감지하는 방식에 있다.

브라우저는 특정 화면 요소에서 이벤트가 발생했을 때 그 이벤트를 최상위에 있는 화면 요소까지 이벤트를 전파시킨다. 따라서, 클래스 명 three -> two -> one 순서로 div 태그에 등록된 이벤트들이 실행된다. 마찬가지로 two 클래스를 갖는 두 번째 태그를 클릭했다면 two -> one 순으로 클릭 이벤트가 동작할 것 이다.

여기서 주의해야 할 점은 각 태그마다 이벤트가 등록되어 있기 때문에 상위 요소로 이벤트가 전달되는 것을 확인할 수 있다. 만약 이벤트가 특정 div 태그에만 달려 있다면 위와 같은 동작 결과는 확인할 수 없다.

이와 같은 하위에서 상위 요소로의 이벤트 전파 방식을 이벤트 버블링이라고 한다.

> 버블 정렬 마냥 버블버블하게 묶인다는 의미에서 버블링으로 네이밈된게 아닐까 생각해본다.