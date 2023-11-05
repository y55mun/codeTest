""" 숫자의 합
https://www.acmicpc.net/problem/11720
"""

N = int(input())
# nums = input()
tmp = [int(i) for i in str(input())[::-1]]
print(tmp)
print(sum(tmp))
