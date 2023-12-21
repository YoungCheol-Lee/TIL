# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    ans_arr = []
    for i, j, k in commands:
        new_arr = array[i-1:j]        # new_arr배열에 array의 i번째~j번째 slicing -> 이때, i번째가 되려면 index 상으로는 -1
        new_arr.sort()                # 정렬
        ans_arr.append(new_arr[k-1])  # ans_arr배열에 정렬한new_arr배열의 k번째(index = k-1) 요소 추가
    return ans_arr


# 힌트: x, y, z = [1, 2, 3] -> 튜플 1 2 3 으로 바로 변경 == Unpacking이라고 부름

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]
