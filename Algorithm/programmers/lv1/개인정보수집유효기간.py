# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 231227 09:30~10:30 1차 실패 ~10:39 성공

# 수집 날짜 + 유효기간 -> 파기
# 모든 달은 28일 까지
# 파기해야할 번호 오름차순 return
# today: 오늘 날짜, terms: 약관 별 유효기간 list[약관종류 몇달], praivacies: 수집된 개인정보 list[날짜 약관종류]
# 날짜는 .으로 구분
# 날짜와 약관종류는 ' '로 구분

def solution(today, terms, privacies):
    # today를 .split(.)으로 나눠서 [연도, 달, 일] 리스트 저장
    today = list(map(int, today.split('.')))
    # terms는 .split()으로 날짜, 약관 나눠서 {약관: [0, 달, 0]} dict 저장
    term_dict = {}
    for term in terms:
        # split ['A', '6'] -> dict{'A': 6}으로 만들기
        term_dict[term.split()[0]] = int(term.split()[1])

    # praivacies도 .split()으로 {약관: [연도, 달, 일, 번호]} dict 저장
    # 약관이 key에 오면, 중복되는 경우에 실패
    priv_dict = {}
    num = 1
    for privacy in privacies:
        # privacy의 날짜를 .으로 .split() -> 연도, 달, 일, 번호 를 int로 바꾸고 list화
        priv_date = privacy.split()[0].split('.')
        for i in range(3):
            priv_date[i] = int(priv_date[i])
        priv_date.append(privacy.split()[1])
        # {번호: [연도, 달, 일, '약관종류']: }
        priv_dict[num] = priv_date
        num += 1

    ans = []
    # praivacies의 val[3]과 terms의 key가 동일 --> praivacies의 달에 terms 달 추가
    for key, val in priv_dict.items():
        # 만약, priv_dict의 val[3]가 term_dict에 있다면 -> term_dict[key]를 val[1]에 더하기
        if val[3] in term_dict:
            val[1] += term_dict[val[3]]
        # 만약, 달 >= 13이면 -> 연도+1, 달-12하기
        # 달=100일 경우에 반복해서 연도+1, 달-12를 해야함
        while val[1] >= 13:
            val[0] += 1
            val[1] -= 12

    for key, val in priv_dict.items():
        # 만약, today가 priv_dict [날짜]보다 더 크다면 -> priv_dict[key][3] 번호를 추가
        if today[0] > val[0]:
            ans.append(key)
        elif today[0] == val[0]:        # 연도가 똑같은데, 달이 더 크면 추가
            if today[1] > val[1]:
                ans.append(key)
            elif today[1] == val[1]:    # 연도, 달이 똑같은데, 일이 더 크면 추가
                if today[2] >= val[2]:
                    ans.append(key)

    return ans
    # if today의 [연도, 달, 일]을 praivacies의 [연도, 달, 일]을 비교 -> today가 더 크면 praivacies의 [번호] pop





print((solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))) # [1,3]
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) # [1,4,5]