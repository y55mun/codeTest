""" 일곱난쟁이
https://www.acmicpc.net/problem/2309
"""

import itertools

seven_list = [int(input()) for _ in range(9)]   # 리스트 컴프리핸션 사용법

for i in itertools.combinations(seven_list, 7): # 7명을 중복 없이 뽑음
    if sum(i) == 100:   # 합이 100이면
        for j in sorted(i): # 7명을 오름차순으로 정렬
            print(j)    # 출력
        break