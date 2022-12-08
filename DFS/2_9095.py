""" 백준 9095: 1, 2, 3 더하기
* 풀이 날짜: 2022-12-07

1. 아이디어
피보나치 수열의 점화식 이용!

2. 시간복잡도


3. 자료구조


"""

import sys
input = sys.stdin.readline

t = int(input())    # 테스트 케이스 개수

def dfs(n):
    if arr[n] > 0 : return arr[n]
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else:
        arr[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
        return arr[n]


for _ in range(t):
    n = int(input())  # 정수
    arr = [0] * (n+1)
    print(dfs(n))