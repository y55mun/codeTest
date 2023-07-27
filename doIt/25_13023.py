"""ABCDE
https://www.acmicpc.net/problem/13023
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
arrive = False  # 정답
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)   # 방문 표시0

# 친구 관계 입력 받기
for _ in range(m):
    s, e = map(int, input().split())
    
    # 친구 관계 등록
    a[s].append(e)
    a[e].append(s)

def dfs(now, depth):
    global arrive
    visited[now] = True
    
    # 친구 관계가 5번 이상 연결 되어 있다면
    if depth == 5:
        arrive = True   # 정답 표시 후 리턴
        return
    
    # 친구 관계가 존재하는지 확인
    for i in a[now]:
        if not visited[i]:  # 아직 방문하지 않았다면
            dfs(i, depth+1)
    visited[now] = False    # 방문 표시 해제

for i in range(n):
    dfs(i, 1)   # 친구 관계 탐색
    if arrive:  # 친구 관계가 존재한다면
        break   # 탈출
if arrive:
    print(1)
else:
    print(0)