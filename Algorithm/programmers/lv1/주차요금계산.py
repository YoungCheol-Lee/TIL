# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 231227 13:20~14:30 1차 실패
# 231227 14:47 성공 -> chat gpt에 물어봄 -> 마지막 주차요금 정산 단계에서 변수로 val를 작성해야 하는데, fee_time이 잘못 들어가 있었음

# 차량번호, 입차, 출차에 따라 요금 계산
# 조건1: 입차 후 출차 내역 없으면 23:59 출차로 간주
# 조건2: 기본 시간 이하면, 기본 요금 청구
# 조건3: 기본 시간 초과면, 기본 요금 + 단위 요금 -> 초과 시간이 단위시간으로 안나눠지면, "올림"=⌈a⌉
# fees: 주차 요금 int list, records: 자동차 입/출차 내역 string list
# fees[0]=기본시간, fees[1]=기본요금, fees[2]=단위시간, fees[3]=단위요금
# records: ["시각" "차량번호" "IN 또는 OUT"]

def solution(fees, records):
    # dict로 {차량번호: [IN 시간, 분]} 받기 (2차원리스트는 탐색에 시간이 오래 걸릴것 같음)
    record_dict = {}
    fee_dict = {}
    fee_list = []
    fee_time = 0
    for record in records:
        # IN/OUT 시간을 int형으로 [시간, 분]
        record_time = list(map(int, record.split()[0].split(':')))
        car_num = record.split()[1]
        # 만약, dict에 차량번호가 존재 -> [OUT 시간, 분] - [IN 시간, 분] 요소끼리 빼고 해당 차량번호key,val 삭제
        if car_num in record_dict: # 이미 dict에 차량번호가 있으면(IN이 들어왔다가 OUT이 확인된 차례)
            fee_time = 0
            # 시간 -> 분으로 모두 바꾸기 -> {'차량번호': 요금시간} 저장
            fee_time = (record_time[0] - record_dict[car_num][0]) * 60 + (record_time[1] - record_dict[car_num][1])
            if car_num in fee_dict:
                fee_dict[car_num] += fee_time
            else:
                fee_dict[car_num] = fee_time

            del record_dict[car_num]
        else:
            record_dict[car_num] = record_time

    # dict에 남은 차량번호(OUT이 없는 차량들) -> 23:59분 기준으로 fee_time 계산
    for key, val in record_dict.items():
        fee_time = (23-val[0]) * 60 + (59-val[1])
        if key in fee_dict:
            fee_dict[key] += fee_time
        else:
            fee_dict[key] = fee_time
        # record_dict에서 차량 삭제

    # 차량번호 오름차순으로 정렬 -> 순서대로 요금 정산
    fee_dict = dict(sorted(fee_dict.items()))
    for key, val in fee_dict.items():
        if val <= fees[0]:
            fee_list.append(fees[1])
        else:
            if (val - fees[0]) % fees[2]:  # 단위시간으로 나눴을 때, 나누어 떨어지지 않으면 -> 올림
                fee_list.append(fees[1] + ((val - fees[0]) // fees[2] + 1) * fees[3])  # 기본요금 + 단위시간 나눈값*단위요금
            else:
                fee_list.append(fees[1] + ((val - fees[0]) // fees[2]) * fees[3])

    return fee_list



print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# [0,591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# [14841]

