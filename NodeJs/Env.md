# env란?

Node.js에서 프로그래밍에 필요한 값들을 서술할 수 있는 .env 환경변수 파일헤 대하여 알아보자.

Node.js에서는 프로젝트 디렉토리에 .둪라는 이름의 파일이 존재하면 환경변수처럼 소스코드로 가져와서 사용할 수 있다.<br />
.env 파일의 내용은 key=value 형태로 써야하며 문장의 맨 앞에 #을 붙이면 주석을 쓸 수도 있다.

```env
# This is sample .env
MESSAGE=hello
NUMBER=1234
```

.env을 이용하기 위해서는 프로젝트에 dotenv 패키지를 설치해야한다.

```js
var express = require("express");
var router = express.Router();

require("dotenv").config();

router.get("/message", function (req, res, next) {
  res.send(process.env.MESSAGE);
});

router.get("/number", function (req, res, next) {
  res.send(process.env.NUMBER);
});

module.exports = router;
```

dotenv 패키지를 불러온 뒤 .config() 함수를 실행하면 .env 파일의 내용을 process.env 객체를 통하여 접근할 수 있다.

MESSAGE 라는 key가 있으면 process.env.MESSAGE 처럼 접근하면 된다.
