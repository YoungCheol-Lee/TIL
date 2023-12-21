# https://school.programmers.co.kr/learn/courses/30/lessons/181931

def solution(a, d, included):
    i, ans = 0, 0
    while i < len(included):
        ans_form = a + d * i
        if included[i] == True:
            ans += ans_form
        i += 1
    return ans

# print(solution(	3, 4, [true, false, false, true, true])) # 37
# print(solution(	7, 1, [false, false, false, true, false, false, false])) # 10
# PyCharm에선 true != True 로 인식하나봄