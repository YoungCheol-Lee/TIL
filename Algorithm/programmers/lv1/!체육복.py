# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 231226 23:45~00:27 1차 실패
# 231227 11:11 성공 -> lost와 reserve 둘다 동시에 확인해야 하는데 if, elif로 진행해서 elif가 pass됨
# set으로 구하는 법 해보기 -> chat gpt 최강....




# 체격 순으로 번호
# 바로 앞, 뒤 번호 학생한테만 빌려주기 가능
# 최대한 많은 학생이 옷입기
# n: 전체학생, lost: 도난 당한 애들 번호 리스트, reserve: 여벌 가진 번호 리스트
# 조건1: 중복 번호 X
# 조건2: 여벌 가진 번호가 도난 -> 하나만 가진게 되므로 빌려주기 X

def solution(n, lost, reserve):
    # dict로 1~n까지 key 만들고, val = 1으로 생성
    # lost 리스트에 해당하는 key -> val -= 1
    # reverse 리스트에 해당하는 key -> val += 1
    # if val = 2이면서 그 전 key의 val = 0이면 ~~
    dict_stu = {}
    cnt = 0
    # dict 1~n까지 만들고, val = 1 생성
    for i in range(1, n+1):
        dict_stu[i] = 1

    for key in dict_stu:
        # lost에 있는 번호면 val-1
        if key in lost:
            dict_stu[key] -= 1
        # reserve에 있는 번호면 val+1
        if key in reserve:
            dict_stu[key] += 1

    # dict 순환 -> .items() 메소드 함수 써야함!!
    for key, val in dict_stu.items():
        # 해당 key의 val가 2일때
        if val == 2:
            # 만약, 첫번호라면 뒷번호 val가 0인지만 확인 (앞 번호 확인하면 에러)
            if key == 1:
                if dict_stu[key + 1] == 0:
                    dict_stu[key] -= 1
                    dict_stu[key + 1] += 1
            # 만약, 앞 번호 val가 0이면
            elif dict_stu[key - 1] == 0:
                dict_stu[key] -= 1
                dict_stu[key - 1] += 1
            # 만약, 마지막 번호라면 앞 번호 val가 0인지만 확인 (뒷 번호 확인하면 에러)
            elif key == n:
                if dict_stu[key - 1] == 0:
                    dict_stu[key] -= 1
                    dict_stu[key - 1] += 1
            # 만약, 뒷 번호가 0이면(앞번호가 0이었으면, if문 탈출해서 상관X)
            elif dict_stu[key + 1] == 0:
                dict_stu[key] -= 1
                dict_stu[key + 1] += 1

    for key, val in dict_stu.items():
        if val >= 1:
            cnt +=1
    return cnt

    # 방법2: set(chat gpt 방법)
    # lost_set과 reserve_set을 서로 차집합
    # reserve_set의 요소 앞, 뒤 번호에 lost_set이 있으면 -> lost_set의 앞 또는 뒤 삭제(reserve_set의 번호 = 체육복 2개인 번호)
    # 최종적으로 남은 lost_set 의 번호만 0 인 상황 -> n - len(lost_set)하면 체육복을 전달 최대값
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        # 여기서 reserve_set(i)는 제거 안해도 되는 이유 -> 어짜피 앞에 주든 뒤에 주든 lost_set의 번호만 신경쓰면 됨
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    return n - len(lost_set)


print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3])) # 4
print(solution(3, [3], [1])) # 2