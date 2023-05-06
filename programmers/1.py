'''


'''

def solution(players, callings):
    player_dic = {p: i for i, p in enumerate(players)}
    idx_dic = {i: p for i, p in enumerate(players)}

    for call in callings:
        cur_idx = player_dic[call]
        front_idx = cur_idx - 1

        cur_player = call
        front_player = idx_dic[front_idx]

        player_dic[cur_player], player_dic[front_player] = front_idx, cur_idx
        idx_dic[cur_idx], idx_dic[front_idx] = front_player, cur_player

    return list(idx_dic.values())