# SERVER_ORM



### Var_routing
URL에 들어온 값을 변수로 사용. **GET 또는 POST**
- GET: 보안 없이, 모두가 볼 수 있음. 주로 검색에만 사용
- POST: 1차적으로 내용은 보안, 받는 사람(URL)은 볼 수 있음.
  - POST 사용 시, html에서 `{% csrf_token %}`을 이용해서 위조를 방지