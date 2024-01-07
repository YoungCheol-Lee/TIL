# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 240107 16:23~16:36

# left~ right 수 사이의 모든 수 순환 -> 각 수의 약수의 개수가 짝수면 더하고, 홀수면 빼기
# 약수의 개수 계산하는 법

def solution(left, right):
    ans = 0
    # left~right 순환
    for num in range(left, right+1):
        cnt = 0
        # 주어진 수의 sqrt 까지 순환 -> 1~sqrt(주어진수)를 각각 나눠서 나머지 == 0 이면 cnt +1
        for i in range(1, int(num**0.5)):
            if (num % i) == 0:
                cnt += 1
        # cnt가 짝수면 더하고 홀수면 빼기
        if (num**0.5).is_integer():
            cnt = cnt * 2 - 1
        else:
            cnt *= 2
        if cnt % 2 == 0:
            ans += num
        else:
            ans -= num

    return ans

print(solution(13, 17))
print(solution(24,	27))