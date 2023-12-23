# Dictonary 정리

## Dictonary 어쩌구저쩌구

- dict 는 index를 사용할 수 없음.


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
