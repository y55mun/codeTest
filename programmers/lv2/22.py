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


""" 다른풀이(BFS)
from collections import deque

def solution(n, computers):            
    
    def BFS(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] and not visited[a]:
                     q.append(a)
                
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
        
    return answer

"""