""" 킹, 퀸, 룩, 비숍, 나이트, 폰
https://www.acmicpc.net/problem/3003
"""

chess_total = [1,1,2,2,2,8]     #킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성

white_chess = list(map(int, input().split()))

for i in range(len(chess_total)):
    print(chess_total[i] - white_chess[i], end=' ')