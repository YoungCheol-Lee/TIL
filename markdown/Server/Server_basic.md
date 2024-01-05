# Server
- Server(서버)는 Request(요청)을 받아 처리하고, 그 결과를 클라이언트에게 Response(응답)하는 역할

## Django
- Django: 파이썬으로 작성된 Web application Framework
    1. Project 내의 APP들을 통해 함수를 Request, Response하여 웹페이지 생성
    2. Model-View-Template(MVT) 패턴을 따름
        - Model: 데이터에 관한 모든 것을 관리. 데이터베이스의 구조를 정의, 데이터 조회, 추가, 수정, 삭제 등을 담당
        - View: 사용자에게 보여지는 부분 및 사용자의 요청을 처리하는 로직 담당. Request을 받아 Model의 함수를 호출, 그 결과를 Template에 전달해 Response
        - Tempalte: 사용자에게 보여지는 부분을 담당. HTML과 DTL(Django Template Language)을 이용하여 웹페이지 생성
    3. 여러 편의 기능: 사용자 인증, 관리자 페이지, 폼처리, RSS 피드, 캐싱, ORM(Object-Relational Mapping) 등

- Django 명령어
```bash
# 새로운 project를 <폴더명>으로 생성
django-admin startproject <폴더명>
# 해당 폴더(Project 또는 Master라고 부름)로 runserver
python manage.py runserver
# 새로운 app 생성
# App을 생성할 때마다, Project폴더의 settings.py의 INSTALLED_APPS리스트에 추가해야함!(, 항상 추가 잊지 말기)
python manage.py startapp

# Project폴더/urls.py
from django.contrib import admin
from django.urls import path, include
# App폴더/urls.py
from django.urls import path
# App폴더/views.py
from django.shortcuts import render
from django.http import HttpResponse
```
> Django를 포함하여 Framework가 무조건 최신 버전이라고 좋은건 아님.   
> 회사에서 신버전을 사용하지 않을 확률이 높고, 버전이 달라지면 엮여 있는 다른 프로그램들이 작동하지 않을 확률이 있음.   

### Django Request-Response 순서
- 먼저, Project폴더 -> APP폴더 -> Template 순서로 Request하며 html 생성

0. Project폴더/settings.py: 새로운 app 추가
1. Project폴더/urls.py: urlpatterns에 원하는 URL문자열 추가
    - `path(<URL문자열>, include('APP폴더명.urls))`
2. APP폴더/urls.py: urlpatterns에 원하는 URL문자열 및 views호출
    - views에서 함수명 호출을 위해 `from . import views` 필요
    - `path(<URL문자열>, views.<함수명>)`
3. APP폴더/views.py: 위의 함수명으로 함수 생성
    - `return render(request, '<html파일명>')`
4. APP폴더/templates폴더생성/<html파일명>: 원하는 html 작성
    - templates 폴더 명은 무조건 `templates`

#### DTL(Django Template Language)
- Django의 템플릿 시스템으로 HTML에서 동적인 데이터 표현을 쉽게 만들고, 코드의 재사용성을 높여줌.   
1. 변수
   - {{` 변수명 `}}
    - `return render(request, '<html파일명>', {})`: {} contest를 추가하여 key: value 추가
    - HTML 에 `{{ key }}`를 입력하면, 웹페이지에 해당 contest의 `value`를 보임

2. 태그
   - {`% for문 or if문  %`} {`% endfor or endif %`}
    - {% %} 를 이용하여 for문 또는 if문을 HTML에서 사용 가능
> `주의!`> {{변수}} 에서 잘못된 key 또는 존재하지 않는 key 를 작성해도 에러가 발생하지 않음!