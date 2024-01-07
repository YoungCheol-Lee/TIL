# https://school.programmers.co.kr/learn/courses/30/lessons/258712 # 24년 겨울 카카오 인턴쉽
# 240106 23:37~01:14 -> 1시간 40분
# 너무 오래걸림. 문제 풀이 방법에 대해 좀 찾아보거나, 30분씩 끊어서 문제 풀이를 할 필요가 있음.


# 이번달까지 선물 주고받은 데이터로, 다음달에 누가 선물을 많이 받을지 예측
# 1. 두 사람이 주고받은 기록이 있다면: 더 적게 준 사람이 선물을 받음
# 2. 두 사람이 주고 받은 기록이 없거나, 주고받은 수가 같다면: 선물지수(선물 준 횟수 - 선물 받은 횟수)가 더 큰 사람이 받음
# 2-1. 선물지수까지 똑같으면 선물 교환 X
# return 선물 가장 많이 받을 사람의 선물 수
# friends: 사람 이름 list (같은 요소 X)
# gifts: "사람1 사람2" 사람1=선물 준 사람, 사람2=선물 받은 사람. 공백으로 구분

def solution(friends, gifts):
    # friends의 요소를 dict{"사람1": [[0, 0, 0], {}], "사람2": [[0, 0, 0], {}]...}으로 만듦
    # [[0, 0, 0], {}] = [[선물 준 횟수, 선물 받은 횟수, 다음달 선물 받을 개수], {교환한 사람: 그 사람에게 선물 준 횟수}]
    friends_dict = {}
    for friend in friends:
        friends_dict[friend] = [[0,0,0], {}]
    # gifts 순환 -> 각 요소 split -> list화
    for gift in gifts:
        give_per = list(gift.split())[0]
        take_per = list(gift.split())[1]
        # 선물 주고 받음 -> 준 사람=check_person[0]=>dict 준 횟수 +1 | 받은사람=check_person[1]=>dict 받은 횟수 +1
        friends_dict[give_per][0][0] += 1
        friends_dict[take_per][0][1] += 1
        # 선물 준 사람: dict{받은사람: 1} | 받은 사람: dict{준사람: 0}
        if take_per in friends_dict[give_per][1]:
            friends_dict[give_per][1][take_per] += 1
        else:
            friends_dict[give_per][1][take_per] = 1
        if give_per in friends_dict[take_per][1]:
            friends_dict[take_per][1][give_per] += 0
        else:
            friends_dict[take_per][1][give_per] = 0

    # dict 2번 순환 -> 특정 사람 vs 다른 사람 비교 -> 다음달 선물 받은 개수 추가
    for now_per in friends_dict:
        for check_per in friends_dict:
            # 자기자신은 continue
            if now_per == check_per:
                continue
            # 선물지수 계산
            now_per_giftnum = friends_dict[now_per][0][0] - friends_dict[now_per][0][1]
            check_per_giftnum = friends_dict[check_per][0][0] - friends_dict[check_per][0][1]

            # 체크하는 사람이 dict{교환한 목록}에 있으면
            if check_per in friends_dict[now_per][1]:
                # 서로 교환한 횟수 체크
                if friends_dict[now_per][1][check_per] > friends_dict[check_per][1][now_per]:
                    friends_dict[now_per][0][2] += 1
                elif friends_dict[now_per][1][check_per] == friends_dict[check_per][1][now_per]:
                    if now_per_giftnum > check_per_giftnum:
                        friends_dict[now_per][0][2] += 1
            # 체크하는 사람이 set{교환한 목록}에 없으면 -> 선물지수 비교
            elif now_per_giftnum > check_per_giftnum:
                friends_dict[now_per][0][2] += 1

    # dict의 다음달 선물 받은 개수 를 내림차순 -> 제일 첫 요소 return
    ans = sorted(friends_dict.items(), key=lambda item: item[1][0][2], reverse=True)
    return ans[0][1][0][2]



print(solution(["muzi", "ryan", "frodo", "neo"],	["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])) # 2
print(solution(["joy", "brad", "alessandro", "conan", "david"],	["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])) # 4
print(solution(["a", "b", "c"],	["a b", "b a", "c a", "a c", "a c", "c a"])) # 0