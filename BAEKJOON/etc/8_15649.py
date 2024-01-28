""" N과 M (1)
https://www.acmicpc.net/problem/15649

1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택
- 재귀함수에서 M 개를 선택할 경우 print

2. 시간복잡도
N! <- 가능

3. 자료구조
- 결과값 저장 int[]
- 방문 여부 체크 bool[]
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
chk = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
recur(0)