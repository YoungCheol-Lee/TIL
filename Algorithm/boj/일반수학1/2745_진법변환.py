# https://www.acmicpc.net/problem/1244

# B진법 수 N -> 10진법으로 바꾸기
# 36진법: 0~9는 숫자로, 10~35는 A~Z로 표현하는 진법
# ex) ZZZAZ -> 10진법: 맨 오른쪽 Z=36^0 * 35(Z가 35이기 때문), 오른쪽에서 2번째 Z=36^1 * 10(A가 10이기 때문)
# 34진법: 0~9는 숫자로, 10~34는 A~X로 표현하는 진법

N, B = list(input().split())

# string N -> list N
nums = list(N)[::-1]
cnt = 0
# 0~9, A~Z 에 0~35 숫자 대응하는 dict 만들기
i = 0
num_dict = {}
a = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for key in a:
    num_dict[key] = i
    i += 1
test = []
for idx, num in enumerate(nums):
    cnt += num_dict[num] * (int(B) ** idx)

print(cnt)
'''입력
ZZZZZ 36
'''
'''출력
60466175
'''