""" 소수찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""

import itertools


def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    ans = []

    for i in range(1, len(numbers)+1):
        nPr = itertools.permutations(numbers, i)
        ans = list(map(''.join, nPr))
        print(set(ans))

    ans_set = set(ans)

    #소수 판별
    for i in ans_set:
        if i == 1:
            break
        else:
            i %

    return answer