""" 트리의 지름 구하기
https://www.acmicpc.net/problem/1167

"""
from collections import deque

import sys
input = sys.stdin.readline
n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n):  # a 인접 리스트에 그래프 데이터 저장
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1

    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        a[s].append((e,v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True   # visited 리스트에 현재 노드 방문 기록
    while q:    # 큐가 비어 있을 때까지 실행
        now_node = q.popleft()  # 큐에서 노드 데이터 가져오기
        for i in a[now_node]:   # 현재 노드의 연결 노드 까지 반복
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append(i[0])

                # 큐에 삽입 된 노드 거리 = 현재 노드의 거리 + 엣지의 가중치
                distance[i[0]] = distance[now_node] + i[1]

bfs(1)  # 임의의 점 1에서부터 시작
Max = 1

for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (n+1)
visited = [False] * (n+1)
bfs(Max)
distance.sort()
print(distance[n])


