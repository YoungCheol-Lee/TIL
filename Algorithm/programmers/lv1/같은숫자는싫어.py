# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 30분, chat gpt 사용
# 마지막 조건에서 문제

def solution(arr):
    ans = []
    i = 0
    # 배열에서 연속된 숫자가 나오면 -> 새로운 리스트에 추가
    while i < len(arr)-1:
        if arr[i] != arr[i+1]:
            ans.append(arr[i])
        i +=1
    # 만약 마지막 2개가 동일한 숫자면, 하나 추가
    # if arr[len(arr)-1] == arr[len(arr)-2]: 를 했는데, 마지막 숫자는 항상 추가되어야함.
    ans.append(arr[len(arr)-1])

    return ans

# pop은 안됨
print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]