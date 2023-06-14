''' 조건 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/181934

'''

def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
