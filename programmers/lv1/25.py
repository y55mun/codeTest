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

    for i in range(1, len(numbers) + 1):
        ans.append(list(set(map(''.join, itertools.permutations(numbers, i)))))
    per = list(set(map(int, set(sum(ans, [])))))

    for i in per:
        if isprime(i) == True:
            answer += 1

    return answer