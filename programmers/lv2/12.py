''' 점프와 순간 이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980

'''

def solution(n):
    ans = 0

    while n > 0:
        ans += n % 2
        n //= 2

    return ans