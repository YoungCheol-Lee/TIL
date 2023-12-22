# swea/4834_숫자카드/4834_sol.py/231222


# input()입력을 파일로 대체
import sys
sys.stdin = open('./sample_input.txt')
### 제출할 때 같이 들어가면 오류남

# Test Case 수 T
T = int(input())
for test_case in range(1, T+1):
    # Test Case 첫 줄에 카드 장수 N(5<=N<=100)
    N = input()

    # 다음 줄에 N개의 숫자 ai(여백X, 0<=ai<=9, 5<=N<=100)
    # 여백이 없으니까 공백을 기준으로 리스트를 나누는 .split()을 하면, 하나의 int정수가 list에 저장됨.
    nums = list(map(int, input()))

    # ai 중에 중복이 가장 많은 수 출력
    # 0~9까지 .count() 반복해서 가장 많은 수를 max_cnt에 [숫자, 중복 수] 저장
    max_cnt = [0, 0]
    for i in range(10):
        cnt = [nums.count(i), i]
        if cnt[0] > max_cnt[0]:
            max_cnt = cnt
        # 중복 개수가 똑같을 경우, 큰 수 출력
        if cnt[0] == max_cnt[0]:
            if cnt[1] > max_cnt[1]:
                max_cnt = cnt
    print(f'#{test_case} {max_cnt[1]} {max_cnt[0]}')





# 출력 결과
# #1 9 2
# #2 8 1
# #3 7 3