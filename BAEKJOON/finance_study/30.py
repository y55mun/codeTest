""" PCCP 기출 1번
https://school.programmers.co.kr/learn/courses/19344/lessons/242258
"""


def solution(bandage, health, attacks):
    max_health = health
    t, x, y = bandage
    end_time = attacks[-1][0]
    cur_t = 0
    cur_health = health

    attacks_dic = dict(attacks)

    for i in range(end_time + 1):
        # 공격
        if i in attacks_dic:
            cur_t = 0
            cur_health -= attacks_dic[i]

            if cur_health <= 0:
                return -1
            continue

        # 공격 받지 않았을 때
        cur_t += 1
        cur_health += x

        # 추가 회복
        if cur_t == t:
            cur_health += y
            cur_t = 0

        cur_health = min(cur_health, max_health)
    return cur_health

bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(bandage, health, attacks))