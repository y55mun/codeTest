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

참고: https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-BOJ-15662-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4-2-Python
"""

import sys
from collections import deque
input = sys.stdin.readline

def solution(T, wheel, k, turn):
    for t, direction in turn:
        turnElement = []

        # t 기준 오른쪽 기어
        for i in range(t+1, T+1):
            if wheel[i][6] != wheel[i-1][2]: turnElement.append(i)
            else: break

        # t 기준 왼쪽 기어
        for i in range(t-1, 0, -1):
            if wheel[i][2] != wheel[i+1][6]: turnElement.append(i)
            else: break

        # t 기어 회전
        wheel[t].rotate(direction)

        # t 기어와 맞닿는 극이 다른 기어 회전
        for element in turnElement:
            # 기준이 되는 톱니바퀴(t)의 바로 양 옆에 있는 것들은 반대로 돌지만,
            # 그게 아닌 한 칸 떨어진 것들은 모두 톱니바퀴 t와 같은 방향으로 회전
            wheel[element].rotate(-direction if (element-t)%2 else direction)
    return sum([wheel[i][0] for i in range(1, T+1)])

T = int(input())
wheel = [0] + [deque(map(int, input().strip())) for _ in range(T)]
k = int(input())
turn = [list(map(int,input().split())) for _ in range(k)]

ans = solution(T, wheel, k, turn)
print(ans)

