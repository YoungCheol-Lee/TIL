# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 240110 20분
# 리스트가 비어있는지 체크 = if not 리스트:

def solution(s):
    check = []
    for i in s:
        if i == '(':
            check.append(i)
        if i == ")":
            # )가 나왔는데, 리스트가 비어 있으면,
            if not check:
                return False
            check.pop()
    if check:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))