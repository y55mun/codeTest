""" 전력망을 둘로 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""
from collections import deque


def solution(n, wires):
    tree = [[] for _ in range(n + 1)]

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    visited = [False] * (n + 1)
    child = [0] * (n + 1)

    def dfs(node):  # 각자의 자식의 개수 구하기
        visited[node] = True

        for next in tree[node]:
            if not visited[next]:
                child[node] += dfs(next) + child[next]

        return 1

    dfs(1)
    result = n

    for c in child:
        result = min(result, abs(n - 2 * (c + 1)))

    return result