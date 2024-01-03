# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 240102 -> 40분 했는데 dict에서 동일한 등수를 벗어나는 방법을 생각 못함
# 240103 -> 1시간 40분 했는데 못품... chat gpt로 1시간 붙잡고 끝냄
# 나중에 꼭 다시 풀어볼 것!

# players: 선수 리스트(중복 X), callings: 해설진이 부르는 선수 명 리스트
# callings에 나온 선수 명은 리스트에서 한칸 앞으로 가야함

# players<=50,000, callings<1,000,000 이므로 리스트 순환은 피해야 할듯?
# dict로 {순서1~마지막:players} 을 하고, callings를 players 리스트 요소 별로 count 해서 숫자 더하기

def solution(players, callings):
    # 선수 이름: 순위 형태의 딕셔너리 생성
    player_dict = {player: i for i, player in enumerate(players)}
    reverse_dict = {i: player for player, i in player_dict.items()}

    # callings를 순회하면서 선수들의 순위를 변경
    for player in callings:
        # player_dict에서 callings에 불린 player의 순위 -1, 이전에 해당 순위였던 overtaken_player의 value +1
        old_rank = player_dict[player]
        overtaken_player = reverse_dict[old_rank - 1]
        # 추월하고 나서 player_dict 순위 업데이트
        player_dict[overtaken_player] += 1
        player_dict[player] -= 1
        # 추월하고 나서 reverse_dict 순위 업데이트
        reverse_dict[old_rank] = overtaken_player  # 추월당하는 선수의 순위를 업데이트
        reverse_dict[old_rank - 1] = player  # 추월하는 선수의 순위를 업데이트

    # 최종 순위를 리스트로 변환
    ans = sorted(player_dict.items(), key=lambda x: x[1])
    ans = [item[0] for item in ans]  # 순위에 따라 선수 이름만 추출

    return ans

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])) # ["mumu", "kai", "mine", "soe", "poe"]
