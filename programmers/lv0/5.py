''' 조건 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/181934

'''


def solution(ineq, eq, n, m):
    answer = 0
    compare = ''

    if ineq == '>' and eq == '=':
        compare = '>='
        if n >= m:
            return 1
        else:
            return 0
    if ineq == '<' and eq == '=':
        compare = '<='
        if n <= m:
            return 1
        else:
            return 0
    if ineq == '>' and eq == '!':
        compare = '>'
        if n > m:
            return 1
        else:
            return 0
    if ineq == '<' and eq == '!':
        compare = '<'
        if n < m:
            return 1
        else:
            return 0