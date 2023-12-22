# swea/4828_minmax/4828_sol.py/231222

# input()입력을 파일로 대체
import sys
sys.stdin = open('./sample_input.txt')
### 제출할 때 같이 들어가면 오류남


# Test Case 수
T = int(input())
for test_case in range(1, T+1):


    # 각 케이스 첫줄에 양수의 개수 N(5<=NN=1000)
    N = int(input())
#    for _ in N:
        # 다음 줄에 N개의 양수 ai(1<=ai<=1,000,000)
        # input한 N개의 정수를 nums에 list화
    nums = list(map(int, input().split()))

    ans = max(nums) - min(nums)

    # 출력: 각 줄마다 "#T"를 출력한 뒤, 답 출력
    print(f'#{test_case} {ans}')


# 출력예시
# #1 630739
# #2 740510
# #3 838110