# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 231226 22:33~23:34
# chat gpt 사용(hash사용 제안) -> dict 힌트 얻음 (사실상 못풀었음)


# 1명을 제외하고 모두 마라톤 완주
# return: 완주하지 못한 선수의 이름 return
# participant: 참여 선수 이름 list, completion: 완주 선수 이름 list
# 조건1: 동명이인 가능성

def solution(participant, completion):
    # participant리스트와 completion 비교 -> 있으면 remove
    # 효율성 테스트 -> participant list의 길이 = 1~100,000 이라 for문 탐색은 불가능

    # dict로 {'participant': 개수} -> completion도 똑같이 진행 -> 동일한 key, 다른 val일 경우 해당 key return
    dict_part = {}
    dict_comp = {}
    ans = []
    for part in participant:
        if part in dict_part:
            dict_part[part] += 1
        else:
            dict_part[part] = 1
    for comp in completion:
        if comp in dict_comp:
            dict_comp[comp] += 1
        else:
            dict_comp[comp] = 1
    for key in dict_part:
        # 만약 dict_part와 dict_key 에서 동일한 key, 다른 val일 때, ans에 해당 key(미완주자 이름)을 추가
        if dict_comp.get(key) != dict_part.get(key):
            ans.append(key)

# 방법1: set을 쓰면 모두 동명이인일 경우에 (set(participant)의 모든 요소 == set(completion)의 모든 요소) 불가능
# 방법2: list.count()로 개수가 다른 요소를 찾으면 O(n^2)이라 불가능
# 이 방법은 O(n^2)이라 효율성 테스트 실패
# if len(set(participant)) == len(set(completion)):
#     for comple in completion:
#         participant.remove(comple)
# else:
#     participant = set(participant)
#     completion = set(completion)
#     ans = list(participant.difference(completion))
    return f"{ans[0]}"




print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # "leo"
print(solution(["marina", "josipa", "nikola", "josipa", "vinko", "filipa"], ["josipa", "filipa", "josipa", "marina", "nikola"])) # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # mislav