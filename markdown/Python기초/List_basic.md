# List 정리

## Lambda 함수 활용
- Lambda 함수란, 간단한 로직의 함수를 한 줄로 표현할 때 사용

1. lambda 표현식
  - 주로 1줄짜리 함수이면서, 여러 번 쓰지 않는 함수일 때, 함수를 만들지 않고 lambda로 바로 사용
  - 매개변수가 1개 이상이면서, return구문 포함 무조건 1줄일 경우 사용 가능

> 맨 앞에 lambda 적기
> def, 함수이름, 소괄호 지우기
> :남기고 엔터, return 지우기

```python
lambda 변수: <코드블럭>

# 예시1: 리스트의 각 요소를 제곱
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
# nums리스트의 각 요소를 x에 받고, 그것을 제곱한 후 list화(map은 함수, iterable변수 로 구성되고, iterable변수의 각 요소에 모두 함수 적용해서 return)
print(squares)  # 출력: [1, 4, 9, 16, 25]


# 예시2: 리스트에서 짝수만 필터링
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # 출력: [2, 4]

# 예시3: 리스트를 특정 기준으로 정렬하는 예제
fruits = ['apple', 'banana', 'cherry']
# 여기서 key 를 사용하는 이유는, 리스트의 각 요소를 입력 받아 정렬에 사용될 값(len(x))를 반환
# 즉, key매개변수를 통해서 어떤 기준으로 정렬할지 결정할 수 있음.
fruit = sorted(fruits, key=lambda x: len(x))
print(fruit)  # 출력: ['apple', 'cherry', 'banana']

```