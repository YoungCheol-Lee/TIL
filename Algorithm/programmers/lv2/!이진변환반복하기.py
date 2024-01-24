# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 240110 00:05분 약 70분
# 2진변환 = bin() 이라는 내장함수를 사용해야함. 또는 주어진 수를 2로 나눈 나머지를 계속 추가, 2로 나눈 몫을 기준으로 반복
# 전역 변수를 함수 안에서 사용하려면, global 을 써야함

# 2진법: n자리 수에서 2^0부터 2^n까지 곱해서 더하기

cnt = 0
num = 0

def solution(s):
    global cnt
    global num
    # 문자열s <= 150,000 이므로 문자열 순환 조심
    # 재귀함수 -> s가 1이 될때까지 이진변환

    # 1. 이진변환 하는법
        # 1-1. 0 제거 -> 0제거한 길이를 2진변환 -> 재귀함수
    cnt += s.count("0")
    s = s.replace("0", "")
    # 2. 재귀함수로 다시 s 이진변환 하는법
    s = bin(len(s))[2:]
    num += 1
    # 3. s가 1이 됐을 때, [이진변환 한 횟수, 삭제한 0의 개수] return
    if s == "1":
        return [num, cnt]
    return solution(s)

print(solution("110010101001")) # [3, 8]
print(solution("01110")) # [3, 3]
print(solution("1111111")) # [4, 1]