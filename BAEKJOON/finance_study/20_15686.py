""" 치킨 배달
https://www.acmicpc.net/problem/15686

아이디어
m개의 치킨집을 선택하는 모든 조합에 대해 도시의 치킨 거리를 구한다!!
치킨 거리: abs(r1-r2) + abs(c1-c2)
"""

import sys
from itertools import combinations

n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]

house = [(i,j) for i in range(n) for j in range(n) if cities[i][j] == 1]
chicken = [(i,j) for i in range(n) for j in range(n) if cities[i][j] == 2]
result = 999999

for chi in combinations(chicken, m):
    temp = 0

    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-chi[j][0])+abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)
print(result)