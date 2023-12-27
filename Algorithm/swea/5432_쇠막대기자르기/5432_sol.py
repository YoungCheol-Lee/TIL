# swea/5432_쇠막대기자르기/5432_sol.py/231227
# chat gpt 사용 -> 스택의 pop, push 이용 -> ')'가 나왔을 때, 2가지 경우에 cnt에 무엇을 더해야 하는지 파악했어야함.

# input()입력을 파일로 대체
import sys
sys.stdin = open('./sample_input.txt')
### 제출할 때 같이 들어가면 오류남


# 조건1: 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# 조건2: 쇠막대기를 다른 쇠막대기 위에 놓을 때, 끝점이 겹치지 않아야 한다(길이가 같은 쇠막대기는 올리기 불가)
# 조건3: 레이저는 모든 쇠막대기의 끝점과 겹치지 않음
# 조건4: 레이저는 반드시 1개 이상 쇠막대기를 자름
# 레이저: '()', 쇠막대기 -> '(' ')'

# Test Case 수
T = int(input())
for test_case in range(1, T+1):
    # 스택의 pop, push 이용
    texts = input()
    check_list = []
    cnt = 0
    for i in range(len(texts)):
        if texts[i] == '(':
            check_list.append(texts[i])
        elif texts[i] == ')':
            # () 레이저 생성 -> ( 1개 pop하고, 길이만큼 cnt에 더하기
            if texts[i-1] == '(':
                check_list.pop()
                cnt += len(check_list)
            elif texts[i-1] == ')':
                check_list.pop()
                cnt += 1

    print(f'#{test_case} {cnt}')
