# MVP이란

MVP 패턴은 Model + View + Presenter를 합친 용어입니다. Model과 View는 MVC 패턴과 동일하고, Controller 대신 Presenter가 존재합니다. MVP 패턴의 구조, 동작, 특징, 장점, 단점을 이야기하겠습니다.

![mvp 패턴 구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FclZlsT%2FbtqBTLzeUCL%2FIDA8Ga6Yarndgr88g9Nkhk%2Fimg.png)

- Model : 어플리케이션에서 사용되는 데이터와 그 데이터를 처리하는 부분입니다.

- View : 사용자에서 보여지는 UI 부분입니다.

- Presenter : View에서 요청한 정보로 Model을 가공하여 View에 전달해 주는 부분입니다. View와 Model을 붙여주는 접착제..? 역할을 합니다.

---

## 특징

Presenter는 View와 Model의 인스턴스를 가지고 있어 둘을 연결하는 접착제 역할을 합니다.

Presenter와 View는 1:1 관계입니다.
