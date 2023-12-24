# Dictonary 정리
딕셔너리는 파이썬의 내장 자료형 중 하나로, 키(key)와 값(value)의 쌍을 갖는 구조를 가짐.   

## Dictonary 생성

- 딕셔너리는 중괄호 `{}`를 사용하거나 `dict()` 함수를 사용하여 생성할 수 있습니다.

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict2 = dict(key1='value1', key2='value2')
```

- dict 는 index를 사용할 수 없음.


## Dictionary 접근
- 딕셔너리의 값을 접근하려면, 대괄호 [] 안에 키를 넣어 사용합니다.
```pyton
print(my_dict['key1'])  # 'value1'
```

## Dictionary 추가 및 수정
- 딕셔너리에 새로운 키-값 쌍을 추가하거나 기존의 값을 수정하려면, 대괄호 []를 사용합니다.
```python
my_dict['key3'] = 'value3'  # 새로운 키-값 쌍 추가
my_dict['key1'] = 'new_value1'  # 기존 키의 값 수정
```

## Dictionary 삭제
- del 키워드를 사용하여 딕셔너리의 키-값 쌍을 삭제할 수 있습니다.

```python
del my_dict['key1']  # 'key1' 키-값 쌍 삭제
```

## Dictionary 메소드
- 딕셔너리는 여러 메소드를 제공합니다. 예를 들어, .keys() 메소드는 딕셔너리의 모든 키를, .values() 메소드는 모든 값을, .items() 메소드는 모든 키-값 쌍을 반환합니다.
```python
print(my_dict.keys())  # 모든 키 출력
print(my_dict.values())  # 모든 값 출력
print(my_dict.items())  # 모든 키-값 쌍 출력
```


### Dict 정렬

- key 기준 오름차순 정렬   
```python
dict(sorted(my_dict.items()))   
```

> 주의! sorted(my_dict.items()) 만 하면 my_dict의 (key, val)가 튜플 형태로 list 정렬됨   

- value 기준 내림차순 정렬   
```python
dict(sorted(my_dict.items(), key=lambda item: item[1], reverse = True))   
```
  - lambda 함수로 item의 index[1]이 value에 해당
  - **reverse = True** 로 내림차순 정렬

> **python 3.7부터 dict 객체는 삽입 순서를 유지함**   
> 
> 즉, value 기준으로 정렬했을 때, 동일한 value가 존재한다면 key의 삽입 순서에 따라 순서가 정해짐
