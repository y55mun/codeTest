""" 아이템 줍기
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102

    # 길찾기
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[0] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = 1

    return answer