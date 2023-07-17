"""연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

import sys
sys.setrecursionlimit(10000) #python이 정한 최대 깊이를 더 깊게 변경해줌
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(v):
    visited[v] = True   # 현재 노드 방문 기록

    for i in a[v]:  # 현재 노드의 연결 노드 중에
        if not visited[i]:  # 방문하지 않은 노드가 있을때만
            dfs(i)  # dfs 함수 실행

for _ in range(m):  # 그래프 데이터 저장
    s, e = map(int, input().split())
    a[s].append(e)  # 양방향 엣지 이므로 양쪽에 엣지 더하기
    a[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)