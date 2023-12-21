# https://www.acmicpc.net/problem/1244

# 스위치 개수
N = int(input())
# 초기 스위치 상태
switches = list(map(int, input().split()))

student_cnt = int(input())

for _ in range(student_cnt):
    # 학생 성별, 받은 숫자
    gender, num = map(int, input().split())
    
    # 남학생일 때
    if gender == 1:
        # num의 배수들을 모두 바꿈(받은 숫자num의 배수 != num의 index의 배수)
        gen1_num = num - 1
        while gen1_num < len(switches):
            if switches[gen1_num] == 0:
                switches[gen1_num] = 1
            else:
                switches[gen1_num] = 0
            # switches[gen1_num] = 0 if switches[gen1_num] else 1 로 줄여 쓰기 가능
            gen1_num += num

    # 여학생일 때
    else:
        # num을 바꾸고, num기준 좌우 대칭인 switch를 모두 바꾼다.
        # 단, 대칭이 아니거나, 0 <= idx < N 일 경우 그만둔다.
        num -= 1    # 받은 숫자에 해당하는 switch의 index와 동일하게 만듦.
        i = 1

        # 받은 숫자 switch 바꾸기
        if switches[num] == 0:
            switches[num] = 1
        else:
            switches[num] = 0
        # switches[num] = 0 if switches[num] else 1 로 줄여 쓰기 가능
        # 또는 switches[num] ^= 1 로 한 줄로 정리 가능!!

        # 좌우 대칭 switch 바꾸기
        while (num-i) >= 0 and (num+i) < len(switches):
            # 대칭이 아니거나, 0 <= idx < N일 경우 그만두기
            if switches[num-i] != switches[num+i]:
                break
            # num기준 좌우 대칭일 경우 switch 바꾸기
            elif switches[num-i] == switches[num+i]:
                if switches[num-i] == 1:
                    switches[num-i] = 0
                    switches[num+i] = 0
                else:
                    switches[num-i] = 1
                    switches[num+i] = 1
                # 여기도 switches[num-i] = 0 if switches[num-i] else 1
                # switches[num+i] = 0 if switches[num+i] else 1 로 줄여 쓰기 가능
            i += 1

# 출력형식: 20개씩 끊어서 출력
ans = ' '.join(map(str, switches))
for x in range(0, len(ans), 40):
    print(ans[x:x+40])
# 출력형식 새로운 방법
# for line_num in range(N // 20 + 1):
#   start = line_num * 20
#   end = (line_num + 1) * 20
#   print(' '.join(map(str, switches[start:end])))

'''입력
41
0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0
2
1 3
2 3
'''