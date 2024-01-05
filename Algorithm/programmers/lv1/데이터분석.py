# https://school.programmers.co.kr/learn/courses/30/lessons/250121
# 240105 30분 1차 정답
# 2차원 list의 정렬에 대해 key=lambda x: x[i] 를 사용하는 방법에 대해 공부 필요


# data: [[코드번호, 제조일, 최대수량, 현재수량], [2번째]..] - 2차원 list
# ext: 어떤 정보를 뽑아 낼지 정하는 - 문자열
# val_ext: 뽑아낼 정보의 기준값 - 정수
# sort_by: 정보를 정렬할 기준이 되는 문자열
# data에서 ext값이 val_ext보다 작은 데이터만 뽑고, sort_by에 해당하는 값을 기준으로 오름차순 정렬 return

# 조건1: data 길이 <= 500
# 조건2: 코드번호 <= 100,000
# 조건3: 정렬 기준에 해당하는 값이 동일한 경우는 없음.

def solution(data, ext, val_ext, sort_by):
    # ext, sort_by의 문자열에 따라 data의 index에 연결하기 위한 변수 생성
    std_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    if ext in std_dict:
        std_num = std_dict[ext]
    if sort_by in std_dict:
        sort_num = std_dict[sort_by]

    ans_list = []
    for i in range(len(data)):
        if data[i][std_num] < val_ext:
            ans_list.append(data[i])
    # 빼낸 리스트의 sort_num에 해당하는 index 기준으로 오름차순 정렬
    ans = sorted(ans_list, key= lambda x: x[sort_num])
    return ans


print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")) # [[3,20300401,10,8],[1,20300104,100,80]]