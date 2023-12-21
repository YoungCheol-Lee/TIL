# Git CLI 버전관리

## Git 버전관리 명령어
```bash
pwd                  # 현재 폴더 위치
ls -al               # 현재 폴더에 있는 내용물(파일, 폴더 등) 출력
mkdir <원하는 폴더명> # 새로운 폴더 생성
cd <생성한 폴더명>    # 생성한 폴더로 들어가기(내가 위치한 곳에 있는 폴더여야함)
git init .           # 내가 들어가 있는 폴더를 git에 올리겠다(init=초기화, .=내가 있는 위치) & .git이란 숨겨진 폴더 생성으로 git에 올릴 수 있음
```

## 버전 만들기
  
> Working tree: 내가 제어(수정)하는 폴더   
> Staging area: git으로 push하길 바라는 폴더(버전을 만들길 원하는 파일)   
> Repository: 만들어진 버전
![git의 3단계](https://miro.medium.com/v2/resize:fit:686/1*diRLm1S5hkVoh5qeArND0Q.png)
- 원리
  - Working tree에서 버전을 만들기를 원하는 파일(폴더)만
  - Staging Area에 보내고, 
  - Staging Area에 있는 파일(폴더)만 하나의 버전으로 Repository에 저장

```bash
touch <원하는파일명>.md<원하는파일확장자>   # 파일 생성
git add <생성한파일명>                    # 해당 파일만 git에 추가하겠다
git commit -m "추가할 내용"               # 해당 파일에 내용 추가
cat <생성한파일명>                        # 파일에 들어있는 내용 확인
git status                               # git에 올라가 있는 내용 확인
git log                                  # git에 올라가있는 내용 확인(q로 나가기)
git log --oneline                        # git log를 한 줄로 정리

git remote add <저장소이름> <저장소주소>
```


