# swea/2001_파리퇴치/2001_sol.py/231221

# input()입력을 파일로 대체
import sys
sys.stdin = open('./input.txt')
### 제출할 때 같이 들어가면 오류남


# Test Case 총 개수
T = int(input())
# 각 Test Case 순환
for test_case in range(1, T+1):
    # N, M을 int형으로 바꿔서 받기
    N, M = map(int, input().split())
    board = []

    # 받은 N에 따라 N X N
    # for _ in range(N):
    #     line = list(map(int, input().split()))
    #     board.append(line)
    # 위 내용을 한줄로 comprehension
    board = [list(map(int, input().split())) for _ in range(N)]
    max_board = 0
    sum_board = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            for i_r in range(M):
                for i_l in range(M):
                    sum_board += board[r+i_r][c+i_l]
            if sum_board > max_board:
                max_board = sum_board
            sum_board = 0

    # 출력 결과
    print(f'#{test_case} {max_board}')