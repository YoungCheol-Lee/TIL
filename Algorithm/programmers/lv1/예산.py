def solution(d, budget):
    d.sort()
    i = 0

    while i < len(d):
        budget -= d[i]
        if budget == 0:
            return (i+1)
        elif budget < 0:
            return i
        i += 1
    return (i)           # budget이 리스트d의 모든 요소를 빼도 남을 경우, 리스트d의 길이=i return




print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4
