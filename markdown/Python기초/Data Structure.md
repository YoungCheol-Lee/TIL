# 데이터 구조(Data Structure)

## 문자열(String)

### 문자열 변경

1. .replace('char1', 'char2')
```python
a.replace('바꿀 문자 대상', '변경할 새로운 문자')
```

2. .strip([chars])
- 공백을 제거하는 메소드
```python
a.strip() # 공백 제거
a.lstrip() # 왼쪽 공백 제거
a.rstrip() # 오른쪽 공백 제거
# 예시
a = 'hihihihahahhihi  '
a.rstrip('hi') # 오른쪽에 있는 hi를 제거(이때는 공백 제거X)
```

3. .split([chars])
- ***문자열***을 특정한 단위로 나누어 ***리스트***로 ***return!!***
- return이므로 해당 string 자체가 list로 바뀜
- 일반적으로 공백을 기준으로 리스트 나눔


1. 'separator'.join(iterable)
- 특정한 문자('separator')를 문자열 사이에 삽입
```python
word = '배고파'
words = ['안녕', 'hello']
!.join(word) # '배!고!파'
!.join(words) # '안녕!hello'
```

```python
# 리스트의 숫자를 하나로 정렬 예시
numbers = [1, 2, 3]
''.join([str(num) for num in numbers])
# numbers에서 1개씩 꺼낸 num을 str type으로 만들기 -> ['1', '2', '3']
# ''.join()으로 각 str 사이에 ''(빈칸)을 삽입 -> '123'
```
  - 주의! 문자열을 쪼개서 리스트에 하나씩 넣음 = list(x)

## 리스트(List)
- String과 List 메소드의 다른점
> String은 메소드함수 자체가 변경된 return값이 있음
> List은 메소드함수가 해당 List를 변경하기만 함(경우에 따라 return이 있기도함)

### 리스트 값 추가 및 삭제
> 많이 쓰는 메소드함수!
1. 리스트.append(x)
- 리스트에 x값 추가

2. 리스트.extend(iterable)
- 리스트.append(x)와 비슷한 결과.   
> extend(['abc'])를 하면 'abc'가 리스트에 들어가고,   
> 또한, extend('abc')를 하면 'a', 'b', 'c'가 따로 들어감   
> 단, append(['abc'])를 하면 ['abc']자체가 리스트에 들어감   

3. 리스트.insert(i, x)
- 리스트에 정확한 위치(index) i에 x값 추가

4. 리스트.remove(x)
- 리스트에서 x값을 삭제 **(x값이 리스트에 없으면 에러)**

> 많이 쓰는 메소드함수!
5. 리스트.pop(i)
- 리스트에서 위치 i(index)에 있는 값을 **삭제** & ***return***
- 자료구조의 스택에서 볼 수 있는 메소드함수

> 즉, return이 있으니까 변수에 pop(i)된 값을 저장 가능
```python
a = ['1', '2', '3', '4', '5']
b = a.pop(0) # 변수b에 a.pop(0)에서 return된 '1'이 저장
```

6. 리스트.clear()
- 리스트의 모든 항목을 삭제
> 리스트 = []로 삭제하는 것과 다른 점
> clear()는 기존의 리스트에서 항목만 삭제(id가 동일)
> 리스트 = []는 새로운 리스트(비어있는 리스트)를 만들기 때문에 id가 다름

### 리스트 탐색 및 정렬

1. 리스트.index(x)
- 리스트에서 x값을 찾고, 해당 index를 return

2. 리스트.count(x)
- 리스트에서 x값의 개수를 반환
```python
# 리스트에서 중복되는 값 삭제 예시
a = [1, 2, 3, 4, 1, 1, 1] # 1이 4번 나옴

for i in range(a.count(1)): #a.count(1) = 0 ~ 리스트a에서 1의 개수 -> range(4) = 0 ~ 3 반복
    a.remove(1) # 4번 반복하면서 1을 삭제 = 1을 4번 삭제

for _ in range(3): # 단순히 n번 반복하는 함수로 쓰고 싶다 = i자리에 _로 놔둬도 됨
    a.remove(1)
```

> 많이 쓰는 메소드함수!
3. 리스트.sort()
- 정렬 메소드함수. 내장함수인 sorted()와 다르게 원본 list가 바뀜
```python
# 로또 번호 정렬
import random
lotto = random.sample(range(1, 46), 6)
# lotto = [1, 22, 41, 42, 23, 26]이라고 가정

print(sorted(lotto)) # 리스트lotto를 정렬. return이기 때문에 리스트lotto = [1, 22, 41, 42, 23, 26]인 상태 유지
lotto.sort() # 리스트lotto 자체를 정렬한 상태로 바꿈(returnX) = 원본 lotto 없어짐 -> 리스트lotto = [1, 22, 23, 26, 41, 42]로 바뀜
```
- 만약 2차원배열 또는 딕셔너리에서 value의 오름차순 정렬이 하고싶다?
```python
def func(item):
  return item[1]

list_a = [[1, 'a'], [2, 'c'], [5, 'b']]
# 만약 2차원 배열에서 2번째 요소인 알파벳문자를 기준으로 sort하고 싶다면?
# def func(item): return item[1] 을 하면, list_a의 요소를 item에 받고, 해당 요소의 index[1]을 return하겠다.
# 즉, func함수를 이용해서 2차원배열 2번째 자리 요소를 오름차순으로 정리 가능
list_a.sort(key=func)
list_a.sort(key=lambda item: item[1])
```


> `주의!` touple은 원래 immutable(불변)한 데이터기 떄문에 사용 불가     

1. 리스트.reverse()
- 반대로 뒤집은 값을 return = [::-1]과 결과는 동일
> .sort()처럼 return값이 없고, 리스트 자체를 바꿈

### 리스트 복사
- 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
```python
#얕은 복사
a = [1, 2, [1, 2]]
b = a[:] # 얕은 복사
a[0] = 5
a[2][0] = 100
print(a) # [5, 2, [100, 2]]
print(b) # [1, 2, [100, 2]]
# b에 리스트a에서 2차원 list가 복사가 안되고, 주소만 복사돼서 a[2][0] = 100 에 영향을 받음
```

```python
from copy import deepcopy # deepcopy 함수 선언
a = [1, 2, [1, 2]]
b = deepcopy(a)
a[0] = 5
a[2][0] = 100
print(a) # [5, 2, [100, 2]]
print(b) # [1, 2, [1, 2]]
# b에 리스트a에서 2차원 list 자체가 전부 복사.
# 2차원 list에서 주로 deepcopy 사용
```

### iterable 타입에 사용 가능한 Built-in Function
> iterable(순회 가능한) type - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

1. map(function, iterable)
  - iterable 구조에서 모든 요소에 각각 funciton을 적용하여 결과를 return

```python
# 예시
# 위의 변수 numbers를 문자열 '123'으로 만드세요. (join 메서드 활용)
numbers = [1, 2, 3]
str_num = [str(num) for num in numbers] 
# 1. numbers에 있는 각 요소들을 for반복문을 num으로 반환
# 2. 모든 num을 str(num)으로 str type으로 반환
# 3. str_num에 [] = list() 리스트 형태로 저장

str_num, ''.join(str_num) # ['1', '2', '3']과 '123'
# ''.join(str_num)에서 리스트str_num의 모든 요소들 사이에 ''를 넣고 연결 -> ''는 빈칸이라 이어져서 나옴
```
> 주의! map메소드함수는 리스트에서 각 요소를 function을 적용하는거지 list로 바꿔주는게 아님.
> 즉, list형태가 필요하다면 list(map()) 또는 [map()]을 해야함

2. filter(function, iterable)
   - iterable 구조에서 모든 요소에 각각 function을 적용하여 반환된 결과가 True인 요소만 return

```python
# 예시
# 홀수를 판별하는 함수가 있습니다.

def is_odd(n): # is가 붙은 함수는 T또는 F를 반환하는 함수 - python에서 약속한 내용
#    for n in nums: 여기서 for반복문 안쓰는 이유 -> 어짜피 filter함수는 iterable(즉, list)구조를 받아서 모든 요소들을 각각 is_odd()함수에 넣기 때문에 for이 있으면 iterable구조가 아닌 int형이 됨
    if n % 2:
        return True
    else:
        return False


result = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
print(result)

# list(filter(lambda n: bool(n%2), [1, 2, 3, 4, 5, 6, 7]))

# 출력 결과: [1, 3, 5, 7]
```

3. zip(*iterables)
  - 여러 개의 iterable 객체를 모아 zip()함.
  - 튜플의 모음을 반환
```python
# 예시
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

list(zip(girls, boys))  # girls와 boys리스트의 index별 요소를 tuple형태로 모아 반환
# 반환 결과: [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

4. lambda 표현식
  - 주로 1줄짜리 함수이면서, 여러 번 쓰지 않는 함수일 때, 함수를 만들지 않고 lambda로 바로 사용
  - 매개변수가 1개 이상이면서, return구문 포함 무조건 1줄일 경우 사용 가능

> 맨 앞에 lambda 적기
> def, 함수이름, 소괄호 지우기
> :남기고 엔터, return 지우기

```python
# 예시
def cube(n):
    return n** 3

type(lambda n: n** 3)
# 둘은 동일
```


---

## 세트(Set)

### 추가 및 삭제

1. .add(요소)
  - 하나의 요소를 추가(중복된 요소는 추가X)
  - 순서는 랜덤

2. .update(*iterable)
  - 여러 값을 추가(***iterable 데이터 구조가 전달인자***)

3. .remove(요소)
  - 하나의 요소 삭제(없는 요소를 .remove()하면 에러 발생)

4. .discard(요소)
  - 하나의 요소를 삭제(없는 요소를 삭제해도 에러 발생X )

> 자주 사용(스택)
5. .pop()
  - 랜덤으로 요소 중 하나를 삭제 (set에 요소가 없는 상태에서 pop()하면 에러 발생)
      - 스택은 가장 위의 데이터 삭제 -> set에선 랜덤 삭제


## 딕셔너리(Dictionary)

### 조회
1. .get(key[, default])   
  - key를 통해 value를 가져옴 (KeyError가 발생하지 않음, default는 기본적으로 None)   

dict[key] = 해당 key에 해당하는 value꺼내기   
dict.get(key) = 해당 key에 해당하는 value 꺼내기   ( default는 기본적으로 None이기 때문에 잘 안적음)   
  - 이때, dict에 없는 key를 꺼내면 dict[key]는 에러 발생 but dict.get(key)는 에러X
      - **에러가 없다고 좋은게 아님!** 뭐가 문제인지 파악을 못함
```python
# 예시
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['apple']                   # key인 'apple'의 value '사과' return

my_dict['pineapple']                # 에러 발생
my_dict.get('pineapple')            # 에러 X

my_dict.get('pineapple', '없는데요') # 해당하는 key가 없을 시 ,뒤에 있는 default 반환
```


### 추가 및 삭제

1. .pop(key[, default])
  - 특정 key가 dict에 있으면, 제거 & 값 return
  - 이때, 특정한 상황이 아니라면 [, default]는 아예 안넣고 .pop(key)만 쓴다.


### dict 순회(반복문 활용)
1. for반복문 활용

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for key in grades:        # 딕셔너리grades에서 key값을 index 0부터 하나씩 반환
    print(key)
    print(grades[key])    # 원래 딕셔너리에서 dict[key]로 해당 key에 해당하는 value 꺼내는 방법 이용


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])
    
    
# 2. `.values()` 활용
# 이 경우 key는 출력할 수 없음
for val in dict.values():
    print(val)

    
# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)

```

- 응용하기(딕셔너리 구축 & counter 사용)
```python
# book_title리스트에서 같은 요소가 몇번 반복 되었는지, {요소:횟수} = {key:value}로 구현
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

counter = {}

# 1번. dict[key]로 접근
for title in book_title:
  if title in counter:     # counter이란 dict에 해당 title요소가 있는가?
    counter[title] += 1    # True -> 딕셔너리counter의 key(=title)의 value += 1
  else:
    counter[title] = 1     # 등장한적 없으면 key = title : value = 1 로 만들기
print(counter)

# 2번. count메소드함수 이용
for title in book_title:
    counter[title] = book_title.count(title)  # key(=title)가 몇 번 나오는지 .count로 찾고 딕셔너리counter에 key = title : value = count된 수

# 3번. get메소드함수 이용
for title in book_title:
    counter[title] = counter.get(title, 0) + 1
    # counter.get()에서 key(=title)이 없으면 -> .get으로 value = 0 을 생성하고, 거기에 +1
    # 만약 특정 key(=title)이 존재 -> 있기 때문에 추가로 +1
    # ex) counter['great'] -> counter라는 딕셔너리에 'great'에 해당하는 부분에 value를 +1 해주겠다.(만약 'great'가 없으면 value = 0을 추가해주고 +1)
print(counter)
```