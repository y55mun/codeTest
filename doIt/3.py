'''구간 합 구하기 4
https://www.acmicpc.net/problem/11659

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in data:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(m):
    s,e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

