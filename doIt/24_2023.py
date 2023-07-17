""" 신기한 소수
https://www.acmicpc.net/problem/2023
"""
import sys
input = sys.stdin.readline

n = int(input())

def isPrime(num):   # 소수 구하기
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:  # 짝수일 경우 소수 제외
                continue
            if isPrime(number * 10 + i):    # i를 뒤에 붙인 새로운 수가 홀수이면서 소수일때
                dfs(number * 10 + i)

# 일의 자리 소수는 2,3,5,7 이므로 4가지 수 에서만 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)
