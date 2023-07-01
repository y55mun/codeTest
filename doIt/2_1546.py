'''평균
https://www.acmicpc.net/problem/1546

'''

n = int(input())
scores = list(map(int, input().split()))
maxx = max(scores)
sum = sum(scores)
print(sum * 100 / maxx / int(n))
