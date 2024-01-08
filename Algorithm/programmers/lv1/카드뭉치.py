# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 240108 20:41~

# 영어단어 카드뭉치 2장
# 조건: 원하는 카드뭉치에서 1장씩 사용 -> 한번 사용한 카드 재사용 X, 카드 무조건 사용, 카드뭉치 순서 바꾸기X
# cards1, 2: 문자열 배열1, 2
# goal: 원하는 문자열 배열

def solution(cards1, cards2, goal):
    # goal요소와 cards1, cards2 0번째 요소
    n = len(goal)
    cards1.reverse()
    cards2.reverse()
    goal.reverse()
    for _ in range(n):
        if goal[-1:] == cards1[-1:]:
            cards1.pop()
            goal.pop()
        elif goal[-1:] == cards2[-1:]:
            cards2.pop()
            goal.pop()
        else:
            return "No"
        if len(goal) == 0:
            return "Yes"

print(solution(["i", "drink", "water"],	["want", "to"],	["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"]))
