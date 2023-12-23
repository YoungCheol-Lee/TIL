# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 231223, 약 50분 소요


def solution(answers):

    # 수포자 1,2,3
    std_1 = [1, 2, 3, 4, 5] * (len(answers)//5 + 1) # answers 와 순환 비교를 위해 길이 맞추기
    std_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    std_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    i = 0 # std 리스트 순환 용도
    cnt_1, cnt_2, cnt_3 = 0, 0, 0 # std_1,2,3 의 맞춘 갯수 비교 변수

    for ans in answers:
        if std_1[i] == ans:
            cnt_1 += 1
        if std_2[i] == ans:
            cnt_2 += 1
        if std_3[i] == ans:
            cnt_3 += 1
        i += 1
    # cnt_1,2,3 중에서 가장 큰 cnt의 번호 리스트 return
    dict_cnt = {}
    cnt_list = [cnt_1, cnt_2, cnt_3]
    # 만약 dict_cnt에 cnt_i가 있다면, value에 번호 i 추가
    for i in range(0, 3):
        # 만약, dict에 cnt_1,2,3이 있으면, value에 번호 i를 append하고
        if cnt_list[i] in dict_cnt:
            dict_cnt[cnt_list[i]].append(i+1)
        # 만약, dict에 cnt_1,2,3이 없다면, 새로운 key와 value를 만들기
        else:
            dict_cnt[cnt_list[i]] = [i+1]

    # key 내림차순 정렬 -> 가장 첫번째 key의 val return
    ans_std = sorted(dict_cnt.items(), reverse=True)
    return ans_std[0][1]


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]