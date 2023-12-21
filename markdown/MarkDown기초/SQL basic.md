# SQL basic

## SQL DB

- sakila, sys, world 등은 DB(DataBase)이다.   
    DB란 하나의 세계관으로 이해, 각 DB에서 실행하는 명령어들은 해당 DB에서만 진행

```
1. SQL 고정 명령어는 대문자, 내가 만든 이름은 소문자(모두 소문자로 적어도 동작은 하지만 Rule을 지키는게 편함)
2. 띄워쓰기와 줄바꿈은 적절히 사용, DB는 신경안씀
3. 주석은 `--`
4. 명령어 끝에는 ;(세미콜론)
5. 명령어 실행 - 명령어 줄에 커서 올리고 ctrl + enter -> 명령어의 범위는 세미콜론 적용 범위
```



## 명령어
### DB 명령어
`CREATE DATABASE pet_shop`: pet_shop이라는 DB를 만들겠다.   
`USE pet_shop`: 만들어진 pet_shop이라는 DB를 사용(좌측 SCHEMAS 옆의 새로고침을 누르고, pet_shop DB를 더블클릭해서 사용 가능)   
`DROP DATABASE pet_shop`: DB 삭제   
`ctrl+t`: 새로운 창 추가 -> ctrl+s로 저장해서 사용

### TABLE 명령어
`CREATE TABLE cats();`: cats라는 table을 생성. 세미콜론은 괄호 뒤에
```sql
CREATE TABLE cats(
    name VARCHAR(50),
    age INT
);
DROP TABLE cats;
DESC cats;
```
`SHOW TABLES`: 내가 보는 DB에서 TABLE을 모두 출력.   
`DESC cats;`: cats라는 table 안에 data 요소를 보여줌   
`DROP TABLE cats`: 특정 테이블 삭제   

```sql
-- 생성된 TABLE에 data 삽입(insert) 명령어
INSERT INTO cats (name, breed, age)
    VALUES  ('먼지', '스코티시폴드', 3),
            ('둘째', '모름', 5),
            ('셋째', '러시안블루', 1);

SELECT * FROM cats; -- TABLE cats의 data출력
```
- 만약 3개를 넣고 싶으면 이렇게 ,로 연결하고 마지막만 ;   
- TABLE cats의 요소인 (name, breed, age)의 변수에 맞춰서 VALUES()를 적어야함   

