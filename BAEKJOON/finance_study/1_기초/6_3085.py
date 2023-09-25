""" 사탕 게임
https://www.acmicpc.net/problem/3085
"""

"""
1. 아이디어
- 브루트포스 사용 -> n <= 50 이므로 가능
한 위치에서 상하좌우와 바꿀 수 있지만 겹치므로 아래와 오른쪽만 계속해서 바꿔주면 된다.
바꿔준 뒤, 전체 보드에서 먹을 수 있는 사탕의 최대 갯수를 구한 뒤 다시 원상복구 해주고
다음 것으로 넘어가 바꿔주고 -> 확인하고 를 반복!

2. 시간복잡도
O(n^4): 50**4 = 6250000 < 2억 => 가능

3. 자료구조
n: int
board: str[][]
maxCnt: int
"""

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input()) for _ in range(n)]
maxCnt = 0

def check():
    global maxCnt
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]


print(maxCnt)