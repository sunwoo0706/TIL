# MVVM이란?

MVVM 패턴은 Model + View + View Model를 합친 용어입니다. Model과 View은 다른 패턴과 동일합니다.

![구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCiXz0%2FbtqBQ1iMiVT%2FstaXr7UO95opKgXEU01EY0%2Fimg.png)

---

- Model : 어플리케이션에서 사용되는 데이터와 그 데이터를 처리하는 부분입니다.

- View : 사용자에서 보여지는 UI 부분입니다.

- View Model : View를 표현하기 위해 만든 View를 위한 Model입니다. View를 나타내 주기 위한 Model이자 View를 나타내기 위한 데이터 처리를 하는 부분입니다.

## 특징

MVVM 패턴은 Command 패턴과 Data Binding 두 가지 패턴을 사용하여 구현되었습니다.

Command 패턴과 Data Binding을 이용하여 View와 View Model 사이의 의존성을 없앴습니다.

View Model과 View는 1:n 관계입니다.
