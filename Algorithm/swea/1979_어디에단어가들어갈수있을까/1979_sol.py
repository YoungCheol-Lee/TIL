# swea/1979_어디에단어가들어갈수있을까/1979_sol.py/231222

# input()입력을 파일로 대체
import sys
sys.stdin = open('./input.txt')
### 제출할 때 같이 들어가면 오류남

# Test Case 수
T = int(input())
for test_case in range(1, T+1):
    # N X N 퍼즐, 단어길이 K input
    N, K = map(int, input().split())
    # puzzle 리스트에 N개의 퍼즐 모양 리스트를 .append()로 받아서, 2차원 리스트로 만든다.
    puzzle = []
    cnt = 0
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    # puzzle[r][c] 순환
    for r in range(N):
        for c in range(N-K+1):
            # puzzle 시작이 1이고, 앞에 0 또는 puzzle 시작일 때(or을 쓰면 c == 0에서 참이면 바로 넘어가니까 out of range가 안나옴)
            if (c == 0 or puzzle[r][c-1] == 0) and puzzle[r][c] == 1:
                # puzzle 길이가 K이고, 뒤에 0 또는 puzzle 끝일 때
                if sum(puzzle[r][c:c+K]) == K and (c+K == N or puzzle[r][c+K] == 0):
                    cnt += 1
    for c in range(N):
        for r in range(N-K+1):
            # puzzle 시작이 1이고, 앞에 0 또는 puzzle 시작일 때
            if (r == 0 or puzzle[r-1][c] == 0) and puzzle[r][c] == 1:
                # puzzle 길이가 K이고, 뒤에 0 또는 puzzle 끝일 때
                # puzzle[r:r+K][c]로 했다가 오류 발생 -> 챗지피티 이용해서 왜 오류나는지 확인
                # [r:r+K]는 row 리스트를 K개 뽑아내기 때문에 index[c]를 특정할 수 없음. [r][c:c+K]는 index[r]번째 리스트 하나를 뽑아내고 [c:c+K] 범위를 찾는거라 괜찮음.
                if sum(puzzle[i][c] for i in range(r, r+K)) == K and (r+K == N or puzzle[r+K][c] == 0):
                    cnt += 1

    print(f'#{test_case} {cnt}')
