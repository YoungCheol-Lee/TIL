# Python-Starter

## 프로그래밍이란?
### 프로그래밍으로 어떤 일을 할 수 있는가
- **언어는 일을 시키기 위한 약속, 문법**

## API, GUI란?
- API: Application Programming Interface   

Database의 출입구 역할
1) private API: 회사 자체 제품과 서비스 개선을 위한 내부 API
2) public API: 개방형 API로 누구나 제한없이 사용 가능한 API
3) partner API: 특정 유저, 기업만 데이터를 공유하는 API

- GUI: Graphic User Interface

## Web이란?

요청(request): URL
응답(response): 문서 한장

- 요청을 한다 = 클라이언트
- 응답을 한다 = 서버
**요청을 URL로 하는 클라이언트**
**응답을 문서로 하는 서버**

> ***모든 Web은 위의 상호작용으로만 구성***

### Requests & Response
먼저, requests는 요청
``` python
import requests
from b4 import BeautifulSoup
# 이걸로 함수 선언하고 시작해야함
```
### 웹크롤링 예시

- python 터미널 열기: ctrl + `
```python
pip install requests beautifulsoup4
# requests랑 beautifulsoup4라는 파이썬 프로그램을 다운하겠다

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'

# naver 증권에 접속하여 전체 페이지를 다운 받는다.
page = requests.get(URL)


#Parsing (구문분석/해석)
data = BeautifulSoup(page.text,'html.parser')

# KOSPI 현재 지수 데이터를 찾아 낸다.
kospi = data.select_one('#KOSPI_now')

# 찾은 데이터를 출력한다.
print(kospi.text) # .text로 양옆 <span>을 떼고 '2,505.07'만 출력
```

1. URL 변수에 웹크롤링 할 주소를 적는다.
2. page라는 변수에 requests함수를 이용해서 URL에 저장된 주소의 전체 정보(코드)를 저장한다.
3. data라는 변수에 BeautifulSoup 함수를 이용해서 


### Telegram Bot 예시
1. 내가 받길 원하는 data를 정한다.
2. Naver날씨의 경우, 네이버 날씨에 들어가서 URL을 변수 Weather_URL에 저장
3. 변수page에 Weather_URL의 모든 소스를 requests.get() -> 웹크롤링
4. 변수data에 page의 data에서 text만 꺼내기 -> Parsing
5. 변수Temp, Weath에 select_one(**F12로 원하는 영역 selector 복사**)을 통해 기온과 날씨 data 저장, message = Temp + Weath로 합치기.
6. Telegram에서 Bot의 정보와 나의 chat_id 정보를 받는다.
7. Telegram API에서 Bot이 나의 chat_id에 sendMessage하는 변수Message_URL 만들기.
8. Telegram의 Bot이 나에게 message의 내용을 보내게 Message_URL requests.

>                               정리   
> 결국 Naver날씨의 URL을 요청, 필요한 데이터(기온, 날씨)만 뽑아내기   
> Telegram에서 Bot이 나의 chat_id에 메세지 보내는 URL을 요청   
> 필요한 데이터(기온, 날씨)를 메세지 보내는 URL로 요청   
> -> 나의 chat_id에 Bot이 필요한 데이터(기온, 날씨)의 문자열을 보냄   



---
```
-더 적어야 할 내용-
-적다가 부족하거나 모르겠는 내용 있으면 추가로 찾으면서 하기-
API GUI 란?
클라이언트 SW => 브라우저 / requests
ctrl + ` | python 파일명 = 실행
Parsing => bs4?
```