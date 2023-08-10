""" 타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""

def solution(numbers, target):
    sup = [0]

    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)

        sup = sub

    return sup.count(target)