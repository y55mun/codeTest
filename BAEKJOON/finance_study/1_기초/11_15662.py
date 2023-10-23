""" 톱니바퀴 (2)
https://www.acmicpc.net/problem/15662

입력:
4
10101111
01111101
11001110
00000010
2
3 -1
1 1

출력:
3
"""

import sys
from collections import deque
input = sys.stdin.readline

def solution(T, wheel, k, turn):
    for t, direction in turn:
        turnElement = []

        for i in range(t+1, T+1):
            if wheel[i][6] != wheel[i-1][2]: turnElement.append(i)
            else: break
        for i in range(t-1, 0, -1):
            if wheel[i][2] != wheel[i+1][6]: turnElement.append(i)
            else: break
        wheel[t].rotate(direction)

        for element in turnElement:
            wheel[element].rotate(-direction if (element-t)%2 else direction)
    return sum([wheel[i][0] for i in range(1, T+1)])

T = int(input())
wheel = [deque(map(int, input().strip())) for _ in range(T)]
k = int(input())
turn = [list(map(int,input().split())) for _ in range(k)]

ans = solution(T, wheel, k, turn)
print(ans)

