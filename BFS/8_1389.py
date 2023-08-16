""" 백준 1389번 케빈 베이컨의 6단계 법칙

- bfs 탐색을 통해 문제를 수행한다.
- 반복문을 통해 모든 친구를 기준으로 탐색한다.
- 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색한다.
- 탐색하면서 탐색하기까지 걸린 횟수를 체크한다.
- 케벤 베이컨의 수가 가장 작은 사람을 인덱스를 이용해서 출력한다.

"""

from collections import deque

def BFS(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()

        # 친구 관계를 확인하고 탐색하지 않은 친구라면 탐색한다.
        for v in edge_list[t]:
            # 탐색하기 위한 횟수를 체크한다.
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)
6

N, M = map(int, input().split())  # N:유저의 수, M: 친구관계 수
edge_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    edge_list[s].append(e)
    edge_list[e].append(s)

queue = deque()
res = []    # 케빈 베이컨의 수를 담는 리스트

# 반복문을 통해 모든 친구를 탐색한다.
for i in range(1, N+1):
    res.append(BFS(i))

# 가장 작은 케빈 베이컨의 수를 가지고 있는 사람의 인덱스 + 1 을 해주어 출력한다.
print(res.index(min(res))+1)