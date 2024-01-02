# HTML_basic
- HyperText Markup Language의 약자   
- 웹 페이지를 작성하는 데 사용되는 표준 마크업 언어   
- 다양한 tag를 사용하여 텍스트, 이미지, 링크, 표 등을 구조화하여 제공

## Intro
! + tab: HTML의 기본 문서 형식을 자동 완성

```html
<!DOCTYPE html>

<html>
    <head>
        <!-- Head > Metadata-->
        <meta charset="utf-8">
        <!-- 문서의 제목(tab 제목으로 활용)-->
        <title>00 Intro To HTML</title>
    </head>

    <!-- Body > 실제 문서 표시됨-->
    <body>
        안녕하세요
    </body>
</html>
```

### Heading
- Mark Down과 비슷한 형식
- <h1>의 숫자 = #의 개수 처럼 구조화 가능


### Content
<p></p>: 문단 형성   

- 특정 데이터나 text를 제공하기 위하여 문단을 나누는 용도

<br>: 문단 내에서 line break(줄 나누기)

- 한 문단에서 내용의 분리가 필요할 때. 단, 여백의 용도로 사용하지 말것.

### Link
`<a href="URL주소" target="_blank">웹페이지에 표시될 text</a>`
target="_blank"는 링크 클릭 시 새 탭에서 열리게 함.   

### List
- Ordered List(순서가 있는 리스트)   
    - `<ol>` 내의 `<li>` 들은 순서에 따라 1, 2, 3번 순서 정렬   
    - `<li>` 내에 들여쓰기로 `<ol>` 작성 시, 리스트 안의 리스트도 가능   
- UnOrdered List(순서가 없는 리스트)
    - `<ul>` 안에 `<ol>`로 순서 형성 가능

```html
    <ol>
        <li>HTML 학습하기</li> 
        <li>복습하기</li>
        <li>마크다운 정리하기</li>
        <li>
            내일 내용 예습하기
            <ol>
                <li>CSS</li>
                <li>Bootstrap</li>
            </ol>
        </li>
    </ol>

    <ul>
        
    </ul>
```

### Table
- 웹페이지의 Table을 구성할 수 있음
- `<table>`
  - `<thead>`: table의 head, 첫 번째 row 담당
  - `<tr>`: `<thead>` 또는 `<tbody>`의 row 1개
  - `<th>` 또는 `<td>`: 위치한 `<tr>`(row)의 각 요소
각 table의 style은 전체 head에 style sheet를 작성하여 구성할 수 있음.

### Media
- 사진 추가 `<img src="이미지파일 이름 또는 URL" alt="사진 설명">`
  - 직접 가지고 있는(local) 이미지 파일 또는 인터넷의 URL을 통해 추가할 수 있음

- 비디오 추가
  - `<iframe>`에서 비디오의 URL과 여러 조건들을 이용해 추가할 수 있음

### Form
- 데이터를 보낼 수 있음. **POST**의 역할
- 아래와 같은 형식, `<div>`로 각 label을 그룹화하고, 원하는 것들을 추가
```html
    <form action="아래 데이터를 보낼 목적지 URL" method="POST">
        <div></div> <!-- div: 아무 특징 없지만, group화 하는 용도-->
        
        <div>
            <label for="username">username</label>
            <input id="username" type="text">
        </div>
        <div id="age">
            <label for="age">age</label>
            <input id="age" type="number">
        </div>
        <div>
            <label for="password">password</label>
            <input id="password" type="password">
        </div>
        <div>
            <label for="email">email</label>
            <input id="email" type="email">
        </div>
        <div>
            <label for="bio">자기소개</label>
            <textarea name="" id="bio" cols="30" rows="10"></textarea>
        </div>
        <!-- 제출 -->
        <div>
            <input type="submit">
        </div>
    </form>
```