## dom event intro

어떠한 event라도 `on:` 지시문를 이용해서 수신할 수 있습니다.

```svelte
<script>
	let m = { x: 0, y: 0 };

	function handleMousemove(event) {
		m.x = event.clientX;
		m.y = event.clientY;
	}
</script>

<div on:mousemove={handleMousemove}>
	The mouse position is {m.x} x {m.y}
</div>
```

다음과 같이 event handler를 인라인에서 지정가능합니다.

```svelte
<div on:mousemove="{e => m = { x: e.clientX, y: e.clientY }}">
	마우스 위치 {m.x} x {m.y}
</div>
```

`""` 따옴표는 선택 사항이지만 구문 강조 표시를 할때 유용합니다.

> 일부 프레임워크에서는 (특히 루프 내부와 같은 성능상의 이유로) 인라인 이벤트 핸들러를 피하라는 권장 사항을 볼 수 있습니다. svelte에서는 어림도 없죠 컴파일러 형식으로 당신이 어떤 방법을 선택하는 항상 옳은 방향으로 실행될 것 입니다.
