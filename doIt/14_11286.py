"""절댓값 힙
https://www.acmicpc.net/problem/11286
"""
from queue import PriorityQueue
import sys

input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if queue.empty():
            print('0')
        else:
            temp = queue.get()
            print(str((temp[1])))
    else:
        queue.put((abs(request), request))
