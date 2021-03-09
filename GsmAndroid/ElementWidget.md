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

## 2) 에디트 텍스트

- Id : 위젯의 이름을 정의
- gravity : 텍스트의 배치를 정의(왼쪽, 오른쪽, 중간 등)
- inputType : 입력될 문자열의 형식 지정(문자, 숫자, 비밀번호 등)
- backgroundTint : 에디트텍스트의 배경색상 지정
- hint : 사용자가 입력하기 전에 미리 보여지는 문자열

## 3) 버튼

- Id : 위젯의 이름을 정의
- backgroundTint : 버튼의 색상 지정
- textAllCaps : 버튼의 영어 텍스트 대문자 지정속성
  - true : 무조건 대문자표시, false : 사용자 입력값으로 표시
- textColor : 문자의 색상을 정의
- text : 버튼에 보이는 문자를 설정
- layer-gravity : 레이아웃 내에서 버튼 배치를 정의(왼쪽, 오른쪽, 중간 등)
