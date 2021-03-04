# 안드로이드 기본 위젯 살펴보기

## 1) 텍스트뷰

> 사용자가 수정할 수 없는 텍스트를 표시하는 뷰

- Id : 위젯의 이름을 정의
- Layout_width(dp) : 레이아웃의 너비 정의
- Layout_height(dp) : 레이아웃의 높이 정의

  - dp : 다양한 해상도에 맞게 크기를 자동으로 조절해줌

- autoLink : `ex : android:autoLink="phone"` 자동으로 조절해줌
- text : 화면에 보여지는 문자열을 입력
- textAppearance : 미리 지정된 타입의 문자크기 선택
- textSize(sp) : 문자의 크기를 정의

  - sp : 해상도와 사용자가 글꼴 크기에 따라 텍스트 크기를 자동으로 조절해줌

- textColor : 문자의 색상을 정의
- lines : 텍스트뷰의 높이를 정의 / 줄바꿈 : ₩n
