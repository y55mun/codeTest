"""네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""

"""
1. 아이디어
- BFS로 풀기

"""

def solution(n, computers):
    answer = 0
    connect = [[0] * n for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if computers[j][i] == 1 or computers[i][j] == 1:
                if i != j:
                    print(i, j)
                    answer += 1

    return answer