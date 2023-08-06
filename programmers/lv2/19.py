""" 전력망을 둘로 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""

from collections import deque


def solution(n, wires):
    answer = 100000

    tree = [[] for _ in range(n + 1)]  # 0번부터 노드가 시작되는 것이 아니기 때문에 +1

    for a, b in wires:  # 양방향 이므로 양쪽 모두 추가
        tree[a].append(b)
        tree[b].append(a)

    for node1, node2 in wires:
        visited = [False for _ in range(n + 1)]

        q = deque()
        q.append(node1)
        result = 1
        visited[node1] = True  # 여기서 부터 시작!
        visited[node2] = True  # 한 방향만 순회 할 것 이므로, 다른 방향도 방문했다고 체크

        while q:
            node = q.popleft()
            for ele in tree[node]:
                if not visited[ele]:
                    result += 1
                    visited[ele] = True
                    q.append(ele)
        min_value = min(result, n - result)
        max_value = n - min_value

        if answer > max_value - min_value:
            answer = max_value - min_value
    return answer