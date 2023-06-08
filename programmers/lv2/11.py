''' 예상 대진표
https://school.programmers.co.kr/learn/courses/30/lessons/12985

'''

def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer