"""네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""

"""
1. 아이디어
- DFS로 풀기

"""

def solution(n, computers):
    answer = 0

    def DFS(i):
        visited[i] = 1

        for com in range(n):
            if computers[i][com] and not visited[com]:
                DFS(com)

    visited = [0 for i in range(len(computers))]

    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer