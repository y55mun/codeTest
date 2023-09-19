""" 일곱난쟁이
https://www.acmicpc.net/problem/2309
"""

import itertools

seven_list = [int(input()) for _ in range(9)]   # 리스트 컴프리핸션 사용법

for i in itertools.combinations(seven_list, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break