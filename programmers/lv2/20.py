""" 모음사전
https://school.programmers.co.kr/learn/courses/30/lessons/84512
"""

from itertools import product

def solution(word):
    answer = 0
    char = ['A', 'E', 'I', 'O', 'U']
    tmp = []

    for i in range(1, 6):
        for j in product(char, repeat=i):
            tmp.append(''.join(j))

    tmp.sort()

    return tmp.index(word) + 1