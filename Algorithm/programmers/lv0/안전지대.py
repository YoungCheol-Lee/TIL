# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 240107 16:41~16:56 약속때문에 잠깐 중단
# 2차원 배열 문제



def solution(board):
    # 리스트 순환 -> 1이 나오면, 주변 0을 x로 바꾸기
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(row):
            if num == 1:
                # 1 인 요소의 index가 0, n-1이면 out of range 신경 쓰기
                if row_idx == 0:
                    board[row_idx+1][col_idx] = 'x'
                if col_idx == 0:

    # 끝나고 0을 count()

    answer = 0
    return answer



print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])) # 13
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])) # 0