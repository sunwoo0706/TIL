## Updating arrays and object

svelte는 값의 할당에 의해 트리거되기 때문에 `push`, `splice` 같은 배열 함수를 사용하면 자동으로 업데이트가 발생하지 않습니다.

그래서 다음코드는 작동하지 않습니다.

```svelte
function addNumber() {
	numbers.push(numbers.length + 1);
}
```

위 문제를 해결하기 위한 방법이 두가지가 있는데있는데

```svelte
function addNumber() {
	numbers.push(numbers.length + 1);
	numbers = numbers;
}
```

위와 같이 중복되는 할당을 추가하거나 (딱봐도 좋아보이지 않는 코드이죠)

```svelte
function addNumber() {
	numbers = [...numbers, numbers.length + 1];
}
```

위와 같은 방법으로 불변성을 지키며 할당해주는 관용적인 방법이 있습니다.

---

배열과 객체의 속성에 대한 할당(예 : `obj.foo += 1`, `array[i] = x`)는 값 할당과 동일한 방식으로 반응성이 작동

```svelte
function addNumber() {
	numbers[numbers.length] = numbers.length + 1;
}
```
