# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 240107 16:41~16:56 약속때문에 잠깐 중단 -> 모르겠음
# 2차원 배열 문제



def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    n = len(board)
    safe_area = n * n - sum(sum(row) for row in board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == 0:
                        safe_area -= 1
    return safe_area


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])) # 13
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])) # 0