""" 디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
import heapq

def solutions(jobs):
    ans, now, i = 0, 0, 0
    heap = []
    start = -1

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            ans += (now-current[1])
            i += 1
        else:
            now += 1

    ans = ans // len(jobs)
    return ans

jobs = [[0, 3], [1, 9], [2, 6]]     #  [작업이 요청되는 시점, 작업의 소요시간]
print(solutions(jobs))