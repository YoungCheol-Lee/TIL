# https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 5분

def solution(n):
    for x in range(2, n+1):
        if n % x == 1:
            return x



print(solution(10)) # 3
print(solution(12)) # 11