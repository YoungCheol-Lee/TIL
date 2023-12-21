# 함수(function)

## 함수의 정의
함수를 쓰는 이유   
  1. 가독성
  2. 재사용성
  3. 유지보수

### 함수의 선언과 호출
```python
def 함수명(매개변수1, 매개변수2, ...):
    <함수 내용 코드 블럭>
    return 반환값 # return이 없으면 반환값이 'None'으로 고정됨!!!
```
- 매개변수는 위치가 정해져있음(위치인자)
- ***return 반환값은 무조건 하나의 객체 반환***
- return이 없으면 반환값 = None 고정
- return이 나오면 해당 함수 바로 종료

---


- 예시1_함수 선언
```python
# 예시1_함수 선언
def greeting(name, age):
    return (f'안녕하세요 저는 {name}, {age}살 입니다.')


greeting('이영철', 24) # 가능(위치인자 맞추기)
greeting(24, '이영철') # 가능(위치인자가 달라서 24, 이영철살 입니다로 출력)
greeting('이영철', 24, '수원') # 불가능(함수의 매개변수는 2개, 전달인자는 3개여서 오류 발생)
greeting(age = 24, name = '이영철') # 가능(위치인자를 선언해서 맞추기)
```
- 예시2_함수 기본 인자값 설정
```python
# 예시2_함수 기본 인자값 설정
def greeting(name = '이영철', age):
    return (f'안녕하세요 저는 {name}, {age}살 입니다.')

greeting('홍길동' 24) # 가능(기본 인자값에 '홍길동' 덮어쓰기)
greeting(24) # 불가능(위치 인자에 따라 24는 age가 아닌 name자리의 기본 인자값을 덮어씀 -> age 매개변수에 해당하는 전달인자가 없음 -> 에러 발생)
```

- 예시3_함수 기본 인자값 설정(오류 발생 피하기)
```python
# 예시3_함수 기본 인자값 설정(오류 발생 피하기)
def greeting(age, name = '이영철'):
    return (f'안녕하세요 저는 {name}, {age}살 입니다.')

greeting(24) # 가능(위치 인자에 따라 24는 age에 해당. name은 기본 인자값으로 '이영철'이 들어가 있기 때문에 매개변수가 모두 할당되어서 에러 발생X)
```

---

## 함수와 스코프(scope)

- 전역 스코프(global scope)
- 지역 스코프(local scope)
- 전역 변수(global variable)
- 지역 변수(local variale): 주로 함수 내에 선언되는 변수. 함수 밖에서 사용 불가.

## 재귀함수(recursive function)
- 자기 자신을 호출하는 함수

1. 팩토리얼 계산
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    # factorial(n)함수 안에 factorial(n-1) 호출 -> 반복하다가 n == 1 일때, return 1 하면서 n * n-1 * n-2 * ... * 1 = n!
```

2. 피보나치 수열
```python
# 피보나치 수열 재귀함수ver
# 1 1 2 3 5 8 13 21 34 55...

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

```python
# 피보나치 수열 while반복문ver
def fib_loop2(n):
    a, b = 0, 1
    
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b
```
- 장점: 반복문보다 `변수 사용 감소`가 될 수 있다.
- 단점: 일부 재귀함수는 반복문보다 `느린 연산속도`를 보인다.


> ***재귀함수를 이용한 문제풀이가 필요할 듯함.***