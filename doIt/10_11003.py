"""최솟값 찾기
https://www.acmicpc.net/problem/11003

예제입력
12 3
1 5_문자열 2 3 6 2 3 7 3 5_문자열 2 6

예체출력
1 1 1 2 2 2 2 2 3 3 2 2
"""
from collections import deque

n, l = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))   # 주어진 숫자 데이터를 가지는 리스트

for i in range(n):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i-l:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')