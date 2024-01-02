# Pandas_basic

## Pandas란?
- numpy 기반으로 만들어진 패키지
- numpy array 구조를 기반으로 Series, DataFrame 객체로 효율적인 자료구조 제공

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