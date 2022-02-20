## 왜 javascript의 달은 0을 기준으로 할까?

javascript는 Date의 월 인수가 0부터 시작해서 11로 끝난다. 하지만 일 인수는 1에서 31 사이의 숫자이다.
왜일까?

이 문제는 javascript의 Date가 Java의 JDK1.0 (1995)의 `java.util.Date`를 카피하였기 때문에 발생하는 일이다.

[자바스크립트를 창시한 브렌든 아이크의 트윗](https://twitter.com/BrendanEich/status/481939099138654209)
