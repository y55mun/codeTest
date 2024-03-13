""" 트리의 부모 찾기
https://www.acmicpc.net/problem/11725
- 푼 날짜: 24-03-13
- 재풀이 날짜:

아이디어
트리를 만든다.
트리를 순회한다.
"""

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())    # 노드 갯수
trees = [[] for _ in range(n+1)]    # 연결 정보 저장
visited = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

visited[1] = 0
q = deque()
q.append(1)

while q:
    cur_node = q.popleft()
    for next in trees[cur_node]:
        if not visited[next]:
            visited[next] = cur_node
            q.append(next)

print('\n'.join(map(str, visited[2:])))