## Statements

svelte의 반응성은 값에만 국한되지 않습니다.
임의의 코드 블럭을 반응성으로 실행 가능합니다.

예를 들어 [반응성 선언](./ReactivityIntro.md)의 예제를 보면

```svelte
let firstname = lee;
let lastname = sunwoo;
$: fullname = firstname + lastname;
```

이 부분에서 firstname이나 lastname이 변경될때마다 콘솔에 로그를 찍을수 있습니다.

```svelte
$: console.log(`the lastname is ${lastname}`);
```

반응성으로 실행시킬 코드 블럭이 길다면 다음의 방법으로도 사용가능합니다.

```svelte
$: {
	console.log(`the lastname is ${lastname}`);
	alert(`I SAID THE LASTNAME IS ${lastname.toUpperCase()}`);
}
```

그리고 마지막으로 반응성 선언을 if 문 앞에서 사용 가능합니다.

```svelte
$: if (lastname.length <= 1) {
	alert(`오 당신은 외자이시군요`);
	lastname += " : 외자";
}
```
