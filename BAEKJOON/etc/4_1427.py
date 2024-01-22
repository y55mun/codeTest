""" 소트인사이드
- 풀이 날짜:
https://www.acmicpc.net/problem/1427
"""
a = list(input())

for i in range(len(a)):
    maxx = i

    for j in range(i+1, len(a)):
        if a[j] > a[maxx]:
            maxx = j
    if a[i] < a[maxx]:
        a[i], a[maxx] = a[maxx], a[i]

for i in range(len(a)):
    print(a[i], end='')