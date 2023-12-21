# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    box_arr = []
    cnt = 0
    for move in moves:              # moves의 요소를 순환
        for row in board:           # board의 row요소 [0,0,0,0,0] -> [0,0,1,0,3]...순환
            if row[move-1] != 0:        # row의 요소에서 move에 해당하는 index = move-1
                box_arr.append(row[move-1])
                if len(box_arr) >= 2:
                    if box_arr[len(box_arr)-2] == box_arr[len(box_arr)-1]:  # if box_arr 마지막 2개가 똑같다면,
                        box_arr = box_arr[:-2]   # box_arr에서 마지막 2개를 slicing한 배열로 덮어쓰기
                        cnt += 2
                row[move-1] = 0              # box_arr에 추가한 row[move-1]을 0 으로 초기화
                break
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4