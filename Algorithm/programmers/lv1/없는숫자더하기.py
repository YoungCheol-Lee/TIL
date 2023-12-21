# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    num_sum = 0
    i = 1
    while i < 10:
        if i not in numbers:
            num_sum += i
        i += 1

    return num_sum

print(solution([1,2,3,4,6,7,8,0])) # 14
print(solution([5,8,4,0,6,7,9])) # 6