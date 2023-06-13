'''홀짝에 따라 다른 값 반환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181935

'''

import math

def solution(n):
    answer = 0

    if n % 2 != 0:
        n = [i for i in range(1, n + 1) if i % 2 != 0]
        return sum(n)
    else:
        n = [i ** 2 for i in range(1, n + 1) if i % 2 == 0]
        return sum(n)