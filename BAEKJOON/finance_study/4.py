""" [PCCP 모의고사 #2] 2번 - 신입사원 교육
https://school.programmers.co.kr/learn/courses/15009/lessons/121688

아이디어
- 원소 중에 가장 작은 원소 2개 찾기 -> sort 를 사용하면 매 순간마다 정렬을 해야해서 시간복잡도가 커짐.
- 두 원소의 합을 구해서 해당 원소들을 업데이트
"""

import heapq

ability = [1, 2, 3, 4]
number = 3

q = []
for a in ability:
    heapq.heappush(q, a)

for _ in range(number):
    x, y = heapq.heappop(q), heapq.heappop(q)
    new = x + y
    heapq.heappush(q, new)
    heapq.heappush(q, new)

return sum(q)