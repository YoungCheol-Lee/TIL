# CLI basic
## CLI 명령어

- `$`: 프롬프트 - 현재 명령어를 받을 준비가 됨   
- `ctrl + c`: 취소(cancle)   
- `ctrl + l` = `clear`: 작성된 명령어 화면 클리어(화면 클리어)   
- `tab`: 자동완성
- `tab tab`: 자동 완성이 가능한 파일명 보여주기

- `touch`: 파일 생성   
    touch **`aaa.txt`** - aaa란 txt파일 생성   
    touch **`.aaa`**.txt - aaa란 txt파일을 생성하는데, 숨김파일   
- `ls`: 현재 폴더의 내용물을 보여줌(list 형식)   
    폴더는 맨 뒤에 /가 붙음(파일은 변화 없음)   
- `ls -a`: 현재 폴더의 모든 내용물 보이기(**-a는 all의 의미**)   
- `rm`: 파일 삭제(remove)   
- `rm -r`: 파일/폴더 모두 삭제   
- `rm -rf`: 파일/폴더 강제 삭제(폴더 내에 파일 있는 경우도 삭제)
- `mkdir`: 폴더 생성(make directory)   
- `rmdir`: 폴더 삭제   
- `cd`: 폴더 이동(change directory)   
    **cd aaa**하면 aaa폴더 안으로 들어간다는 이야기   
- `cp`: 파일 복사 (copy)   
    `cp -r`: 파일/폴더 복사   
- `..`: 상위 폴더로 이동   
- `~`: 홈 폴더의 상징 기호   
    **홈 폴더=로컬디스크C의 사용자 폴더**
    **cd ~ 를 하면 홈폴더로 이동**   
- `/`: root 폴더=홈 폴더의 상위 폴더

---

## Operating System(운영체제)

|Unix(유료)|Unix(유료)|Windows|
|:---:|:---:|:---:|
|Linux(Unix파생)|Apple(유료)|MS-Dos|
|Ubuntu(free)|IOS|Windows 98|
|cent OS(free)|Mac Os|XP|
|Android(free)|Ipad Os|7|
||Vision Os|10|
|||11|

```
위의 CLI basic 명령어는 Unix 파생임.
Windows의 cmd에서 ls와 같은 명령어를 사용하면 인식X.
따라서 Linux, Windows 개발자도 Unix 사용해야할 경우도 있음
```

