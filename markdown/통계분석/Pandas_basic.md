# Pandas_basic

## Pandas란?
- 수치형 테이블과 시계열 데이터를 조작하고 운영하기 위한 파이썬의 **데이터 분석 라이브러리**   
- numpy array 구조를 기반으로 Series, DataFrame 객체로 효율적인 자료구조 제공
- 즉, 파이썬에서 `표 데이터`를 분석하고 처리하기 위한 툴

```python
# pandas 실행
import pandas as pd
# csv파일 읽기
df = pd.read_csv('./<폴더명>/<csv파일명>', index_col='<첫번째 컬럼명>')

```

## Array vs List
- Array 특징   
1. 사이즈가 고정(RAM 낭비가 심함)
2. Array의 요소간 위치가 서로 옆 주소에 존재
3. 실행 속도가 빠름(장점)
- List 특징
1. 사이즈가 가변(RAM 낭비 감소)
2. List의 요소간 위치가 무작위

### 이산형 변수 vs 연속형 변수
- 이산형 변수
1. 인접한 숫자 사이에 값이 존재 X
   -  ex) 주사위의 눈 - 1, 2, 3, 4, 5, 6 사이에 1.5 라는 값 존재 X
   
- 연속형 변수

### Series
- 1차원 ndarray와 비슷한 형태이나, 호환 X
- 1차원 array를 생성하면, index가 자동 생성
```python
# pandas 선언
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
# 출력 결과
#  index 요소
#   0    0.25
#   1    0.50
#   2    0.75
#   3    1.00
```

### DataFrame
- dict 형태의 자료를 2차원 배열로 생성
- Series 객체의 확장. column에 index, key, val1, val2, val3..가 생성
- CSV, Excel, 데이터베이스 등 데이터로드를 위한 도구 존재

```python
import pandas as pd
from pandas import Series, DataFrame

population_dict = {
    'california': 333333333,
    'texas': 111111111,
    'new york': 222222222,
    'florida': 444444
}

area_dict = {
    'california': 86122,
    'texas': 21133,
    'new york': 91531,
    'florida': 77821
}
df = pd.DataFrame({'population': population, 'area': area})
# 출력 결과
#             population   area
# california   333333333  86122
# texas        111111111  21133
# new york     222222222  91531
# florida         444444  77821
```