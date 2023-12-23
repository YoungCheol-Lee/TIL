# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 231223

# 조건: 1<=stages<=N+1, N+1은 N번째 스테이지 까지 클리어한 사용자
# 조건: 실패율이 같은 스테이지 -> 작은 번호가 먼저 오기
# 조건: 스테이지 도달한 사용자X -> 실패율 = 0
# 조건: 해당 스테이지 실패한 사용자X -> 실패율 = 0

# 스테이지 개수: N, 현재 도달한 스테이지 번호 리스트: stages
def solution(N, stages):

    user = len(stages)
    fail_dict = {}
    # 1부터 N까지 순환
    for i in range(1, N+1):
        fail_cnt = 0
        # 해당 스테이지 실패자 카운트
        fail_cnt = stages.count(i)
        if fail_cnt == 0:
            # key = i(스테이지), value = 0(실패율)으로 저장
            fail_dict[i] = 0
        else:
            fail_dict[i] = fail_cnt/user # 스테이지 : 실패율 로 저장
            user -= fail_cnt # 실패한 유저 제외
            fail_cnt = 0 # 초기화
    # fail_dict를 "val(실패율)" 기준으로 "내림차순" 정렬
    fail_dict = dict(sorted(fail_dict.items(), key = lambda item: item[1], reverse = True))
    # 각 val 중에 동일한 val가 있으면, key가 작은 것을 앞으로
    # python 3.7부터 dict 객체는 삽입 순서를 유지함 -> 스테이지 1번부터 N번까지 key에 넣었으니, 내림차순 정렬에서 value가 동일한 key들은 먼저 넣은(낮은 스테이지) 순서대로 정렬됨.

    # 실패율이 높은 스테이지 부터 "내림차순"으로 "리스트" return
    return list(fail_dict.keys())

# 실패율 = 스테이지 도달&클리어X 수 / 스테이지 도달 수

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print((solution(4, [4,4,4,4,4]))) # [4,1,2,3]