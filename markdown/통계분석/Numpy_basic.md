# Numpy_basic

## Numpy란?
- 파이썬의 n차원 배열을 쉽고 효율적으로 사용할 수 있도록 지원하는 패키지(주로 Pandas와 함께 자주 사용)   
- 행렬, 수학적, 논리적, 정렬, 선택, 통계, 시각화 등을 도와주는 도구   

장점   
  1. list 보다 메모리 공간을 덜 차지(모든 요소들의 타입이 dtype)   
  2. array는 크기가 정해져 있으므로, index도 정해져있음 -> list보다 계산이 빠름   

단점   
  1. array는 생성 이후 크기 변경이 불가능(변경이 필요하면 새로운 array 생성하고 복사 붙여넣기 해야함)

## Numpy 사용법

1. 설치
```bash
pip install numpy
```
2. numpy 선언 및 numpy array 생성
```python
import numpy as np

arr = np.array([1,2,3,4], [5,6,7,8]) # 2차원 array
C = A * B # numpy에서의 행렬 곱셈

# list에서의 행렬 곱셈
for i in range(x):
    for j in range(y):
        C[i][j] = A[i][j] * B[i][j]

```

### List와 다른 명령어

- np.zeros(x, y, z): 요소가 0, `x` x `y` array 를 `z`개 생성
- np.arange(x): 0~x까지 1차원 array 생성
- arr1 * arr2: +, -, *, /, ** 등 array끼리 연산자 사용 가능
- arr[x:y] = z: array의 `x`~`y` 요소를 slicing하고 모두 `z`로 변경   
- arr[[x, y, z]]: 기존 array의 `x`, `y`, `z`번째 index에 있는 요소(또는 row)를 순서대로 새로운 array를 재배치해서 제공   
    - arr[[-1, -3, -5]]: -는 뒤에서 1번째, 3번째, 5번째를 의미