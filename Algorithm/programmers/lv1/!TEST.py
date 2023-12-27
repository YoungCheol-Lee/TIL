def solution(bandage, health, attacks):
    # 시전시간, 초당 회복량, 추가회복량, 최대체력, 현재체력, 회복시간, 현재시간 변수 설정
    attack = dict(attacks)

    print(list(attacks.keys())[-1])

#    for time in range(1, list(attack.keys())[-1] + 1):
#        print(time)



print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))