# OOP(객체 지향 프로그래밍)
- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)
- 클래스(Class)와 객체(Object)

## 객체
> python의 ***모든 것은 객체***라고 부를 수 있음
> 모든 객체는 ***타입(type), 속성(attribute), 조작법(method)***를 가짐

### 타입(Type)과 인스턴스(Instance)
> **모든 객체는 특정 타입을 갖는 인스턴스**
a = 10, b = 20 에서 a, b는 객체   
  - **a, b는 int 타입의 인스턴스**

### Method
> 특정 객체에 적용할 수 있는 행위
- <객체>.<메서드>()   
dir()를 하면 ()안의 타입의 객체가 할 수 있는 모든 속성과 메서드를 보여줌

## 객체 지향 프로그래밍
> 단순하게, **"객체를 지향하는 프로그래밍"**

- 절차 중심 vs 객체 중심   
절차 중심: if문 처럼 정해진 절차를 따라 진행   
객체 중심: class와 같이 객체를 분류하여 직관적인 코드 분석이 가능   

### 클래스(Class)와 인스턴스(Instance)
> class: 객체를 분류하는 키워드(울타리)   
> instance: 객체의 예시(내용물)   

- class 와 instance 선언 및 사용 예시
```python
class <클래스이름>:
    <코드블럭>

class Person:            # Person: 클래스
    def talk(self):      # talk(self): 메서드 함수
        print('안녕')

p1 = Person()            # p1: 인스턴스
```

- **self(인스턴스 자기자신)**   
python에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자기 자신이 전달되게 설계   

```python
# self 예시
class Person:
    def test(self):
        return self
p1 = Person()
p1.test() is p1 # True
# 즉, p1 을 self 를 return 하면 p1 의 정보(주소)를 불러옴
```

- **__init__ 메서드 함수**   
인스턴스 객체가 생성될 때, 동시에 return되는 함수   
반드시 `__init__` 이라는 이름으로 정의   
   
- **속성(Attribute) 정의**   
특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 데이터   
`self.<속성명> = <값>` 또는 `<인스턴스>.<속성명> = <값>`으로 설정  
  - 쉽게 설명하면, class 안의 def(메서드 함수)도 기존 def함수처럼 여러 매개변수(속성) 부여 가능   

```python
class Person:
    def __init__(self, name, age): # name, age 가 속성
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'안녕, 나는 {self.name}')

p1 = Person('이영철', 20)        # __init__함수에 name, age 매개변수에 해당하는 전달인자('이영철', 20)을 보냄
p1.name, p1.talk()               
# 객체의 속성의 데이터를 보고 싶으면 <객체>.<속성>
# method를 하고 싶으면 <객체>.<메서드>() 로 ()붙여야함
```

- **매직 메서드**   
`__init__`처럼 `__<메서드>__` 형태 = 매직 메서드   

```python
# 예시

class Person:
    def __str__(self):
        return '객체 출력(print)시 보여줄 내용'
# __str__(self): str 을 print 하는 매직 메서드

```


### 인스턴스(Instance) 와 클래스(Class) 변수

#### 인스턴스 변수
- 인스턴스의 속성(Attribute)   
- 각 인스턴스들의 고유한 변수   
- 생성자 메서드에서 `self.<변수명>` 으로 정의   
- 인스턴스가 생성된 이후 `<인스턴스>.<변수명>` 으로 접근 및 할당   

#### 클래스 변수
- 클래스의 속성(Attribute)
- 모든 인스턴스가 공유 (전역 변수와 비슷한 의미)
- 클래스 선언 내부에서 정의
- `<클래스>.<변수명>` 으로 접근 및 할당   

```python
# 예시
class Circle:
    pi = 3.14

print(Circle.pi)
c1 = Circle()
c1.pi = 4           # 객체ci의 pi변수에 4를 새로 할당
print(ci.pi)        # 4
Circle.pi = 100     # 클래스Circle 의 pi변수 에 100할당
print(Circle.pi, c1.pi) # (100, 4)

# 즉, 객체ci의 pi변수에 할당하는 것과 클래스Circle 의 pi변수에 할당 하는 것은
# 클래스와 객체의 pi변수에 서로 다른 값을 할당하는 것이다.
```

