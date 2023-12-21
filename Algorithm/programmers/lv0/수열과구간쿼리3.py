# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    tmp = 0
    for query in queries:
        tmp = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = tmp
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]])) # 	[3, 4, 1, 0, 2]
# 20분
# 문제 이해 부족 -> query[0]이 arr의 index인데 arr의 요소로 판단했음