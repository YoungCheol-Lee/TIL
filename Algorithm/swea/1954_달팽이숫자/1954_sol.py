# swea/1954_달팽이숫자/1954_sol.py/231221

# input()입력을 파일로 대체
import sys
sys.stdin = open('./input.txt')
### 제출할 때 같이 들어가면 오류남

# Test Case 총 개수
T = int(input())
# 각 Test Case 순환
for test_case in range(1, T+1):
    N = int(input())
    # 0으로 채워진 N X N board 형성 -> 챗지피티 이용..
    board = [[0]* N for _ in range(N)]

    # 시계 방향    우  하  좌  상
    delta_rows = [0, 1, 0, -1]
    delta_cols = [1, 0, -1, 0]
    # 원형 큐 방법 사용
    idx = 0
    row, col = 0, 0
    num = 1

    while num <= N ** 2:
        # 턴을 해야 한다면?
        # board 범위 끝에 도착 or 다음 idx가 숫자가 이미 채워져 있다면
        if row+delta_rows[idx] == N or col+delta_cols[idx] == N:
            idx = (idx + 1) % 4
        elif col == 0 and row == N-1:
            idx = (idx + 1) % 4
        elif board[row+delta_rows[idx]][col+delta_cols[idx]] != 0:
            idx = (idx + 1) % 4

        # 숫자를 채워야 한다면
        board[row][col] = num
        num += 1
        # 우: row 고정 & col +1 / 하: row +1 & col 고정 / 좌: row 고정 & col -1 / 상: row -1 & col 고정
        row = row + delta_rows[idx]
        col = col + delta_cols[idx]

    # 출력 결과
    print(f'#{test_case}')
    for row in board:
        print(' '.join(map(str, row)))