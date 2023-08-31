""" 신기한 소수
https://www.acmicpc.net/problem/2023
"""

import sys
input = sys.stdin.readline

n = int(input())

def isPrime(num):
    for i in range(2, (num/n)+1):
        if num%i == 0:
            return False

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if number %2 == 0:
                continue
            else:
                DFS()   # DFS 탐색 필요
