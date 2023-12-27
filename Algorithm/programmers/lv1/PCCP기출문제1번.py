# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# 231227 21:11~22:00 1차 실패 -> 22:08 성공: 현재체력<0이 될때 return -1 에서 현재체력=0일 때 고려 안함

# t초 동안 붕대 감기, 1초당 x만큼 체력 회복
# t초 연속 성공 -> y만큼 추가 회복
# 조건1: 최대 체력 존재
# 조건2: 붕대감기 도중 공격 당하면 취소 -> 다시 붕대감기 시작(연속 성공 시간 = 0으로 초기화)
# 조건3: 공격 받으면 피해량 만큼 감소
# 조건4: 공격시간은 공격을 하는 시간을 의미.

# bandage: [시전시간, 초당 회복량, 추가 회복량], health: 최대 체력, attacks: [[공격시간, 피해량] ... ] 2차원 list


def solution(bandage, health, attacks):
    # 시전시간, 초당 회복량, 추가회복량, 최대체력, 현재체력, 회복시간, 현재시간 변수 설정
    heal_extra_time, heal_per_sec, heal_extra = bandage
    heal_time = 0
    max_health, now_health = health, health
    attack = dict(attacks)

    for time in range(1, list(attack.keys())[-1] + 1):     # attacks의 마지막 key = 총 시간
        # if 현재시간 in attacks면 -> 현재체력 - attack[현재시간], 회복시간=0초기화
        if time in attack:
            now_health -= attack[time]
            heal_time = 0
        # else(공격 당하면, 회복 안하고 넘어감): 현재체력+초당 회복량
        else:
            now_health += heal_per_sec
            heal_time += 1
            # if 회복시간 == 시전시간 이 되면: 추가회복량 만큼 더 회복, 회복시간=0초기화
            if heal_time == heal_extra_time:
                now_health += heal_extra
                heal_time = 0
            # if 현재체력>최대체력이면: 현재체력 = 최대체력 으로 초기화 (아니면 처음부터 현재체력이 최대체력보다 높아질 수 없게끔 만들거나?)
            if now_health > max_health:
                now_health = max_health

        # if 현재체력<0: return -1
        if now_health <= 0:
            return -1

    return now_health


# print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) # 5
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # -1