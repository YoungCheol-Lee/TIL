# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# 231227 22:11

# 조건1: 가장 작은 index의 파일 ~ 가장 큰 index의 파일까지 최대, 최소 index
# 최소 칸 선택으로 가장 많은 파일 return
# wallpaper: 바탕화면 격자판(1차원 string list) -> 빈칸:".", 파일:"#"


def solution(wallpaper):

    # 2차원 list를 만들고, 각 칸에 wallpaper 넣기
    wallpaper_list = []
    for i in wallpaper:
        wallpaper_list.append(list(i))
    # 처음row, 처음col, 마지막row, 마지막col 변수 생성
    initial_row, initial_col, final_row, final_col = len(wallpaper_list), len(wallpaper_list[0]), 0, 0
    # 2차원 list 순환 -> # 나올때 마다 index[][]에서 가장 작은 row, col 나올때마다 처음row, 처음col에 저장
    # 2차원 list 순환에서 index와 value -> enumerate() 사용
    for row_index, rows in enumerate(wallpaper_list):
        for col_index, file in enumerate(rows):
            if file == '#':
                # index[][]에서 가장 작은 row, col 나올때마다 처음row, 처음col에 저장
                if initial_row > row_index:
                    initial_row = row_index
                if initial_col > col_index:
                    initial_col = col_index
                # 똑같이 가장 큰 row, col 나올때 마다 마지막row, 마지막col에 저장
                if final_row < row_index:
                    final_row = row_index
                if final_col < col_index:
                    final_col = col_index
    # return [처음row, 처음col, 마지막row+1, 마지막col+1]
    ans = [initial_row, initial_col, final_row + 1, final_col + 1]
    return ans




print(solution([".#...", "..#..", "...#."])) # [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])) # [1, 3, 5, 8]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])) # [0, 0, 7, 9]
print(solution(["..", "#."])) # [1, 0, 2, 1]