# https://school.programmers.co.kr/learn/courses/30/lessons/12930

# def solution(s):
#     new_lists = s.split()
#     ans = ""
#     i = 0
#
#     for new_list in new_lists:
#         while i < len(new_list):
#             if (i%2) == 0:
#                 ans += new_list[i].upper()
#             else:
#                 ans += new_list[i].lower()
#             i += 1
#
#         ans += " "
#         i = 0
#     ans = ans.rstrip()
#     print(type(ans))
#     return ans

# 만약 공백이 2개 이상일 경우는 제대로 실행될까? -> 안될거 같은데? -> 다시 새로운 방법으로 생각하기
# 그럼 공백 추가를 고려하면서, upper()과 lower()를 홀수, 짝수 결정 짓는 코드블럭을 만들어보자

def solution(s):
    idx = 0
    new_str = ''
    for char in s:
        if char == ' ':
            new_str += char
            idx = 0
            continue

        if idx % 2:
            new_str += char.lower()
        elif idx%2 == 0:
            new_str += char.upper()
        idx += 1
    return new_str



print(solution("try hello world")) # "TrY HeLlO WoRlD"