# swea/4836_색칠하기/4836_sol.py/231222
# 60분? 처음에 2차원 list로 받고, set으로 중복 제거하면서 sqr_red와 sqr_blue 요소를 비교하려 했으나, 실패
# 강사님 질문 대답으로 모든 좌표를 0으로 만드는 방향으로 다시 접근

# input()입력을 파일로 대체
import sys
sys.stdin = open('./sample_input.txt')
### 제출할 때 같이 들어가면 오류남

# Test Case 수
T = int(input())
for test_case in range(1, T+1):
    # 칠할 사각형의 개수
    N = int(input())
    cnt = 0
    # 9 X 9 좌표판 만들기
    sqr_list = [[0 for r in range(10)] for c in range(10)]
    # N개의 사각형 만들기
    for i in range(1, N+1):
        # row1부터 row2까지, col1부터 col2까지 color(1 또는 2)로 input
        row1, col1, row2, col2, color = list(map(int, input().split()))
        # 입력값의 row1부터 row2까지, col1부터 col2까지 color(1 또는 2)로 채우기
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                # 입력 받은 row, col 모든 요소를 점검 -> color 입력값=1 or 2 일때로 나누기
                if color == 1:
                    if sqr_list[r][c] == 0:
                        sqr_list[r][c] = 1
                    elif sqr_list[r][c] == 2:
                        sqr_list[r][c] = 3
                else:
                    if sqr_list[r][c] == 0:
                        sqr_list[r][c] = 2
                    elif sqr_list[r][c] == 1:
                        sqr_list[r][c] = 3
    for r in range(10):
        for c in range(10):
            if sqr_list[r][c] == 3:
                cnt += 1

    print(f'#{test_case} {cnt}')