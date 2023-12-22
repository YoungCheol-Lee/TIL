# swea/4831_전기버스/4831_sol.py/231222

# input()입력을 파일로 대체
import sys
sys.stdin = open('./sample_input.txt')
### 제출할 때 같이 들어가면 오류남

# Test Case 수
T = int(input())
for test_case in range(1, T+1):

    # 버스: 1번에서 N번 정류장까지 이동, 이동 거리 K
    # 다음 줄에 버스 이동거리 K, 마지막 정류장 번호 N, 충전기 수 M -> K N M 문자열
    K, N, M = map(int, input().split())
    # 그 다음 줄에 충전기 위치 문자열
    chargers = list(map(int, input().split()))

    move = K
    cnt = 0
    # charger와 move를 비교
    for charger in chargers:
        for i in range(1, K+1):
            if move in chargers or move == charger:
                move += K
                cnt += 1
                break
            # 만약 K만큼 이동했는데, 충전기가 없다 -> 그 전 한칸에 충전기 있는지 확인
            elif move > charger:
                move -= 1
                continue
            # 만약 K번 반복 했는데도 충전기가 없다 -> cnt = 0 출력
            else: # move < charger:
                cnt = 0

        # 마지막 정류장 N 도착 시 끝.
        if move >= N:
            break
    # 출력: #test_case 최소 충전 횟수
    print(f'#{test_case} {cnt}')