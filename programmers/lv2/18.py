""" 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""

from itertools import permutations

def solution(k, dungeons):
    answer = -1

    for permute in permutations(dungeons, len(dungeons)):
        hp = k  # 최대 피로도
        count = 0   # 돌 수 있는 던전의 수

        for pm in permute:

            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
            if count > answer:
                answer = count

    return answer
