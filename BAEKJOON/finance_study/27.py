""" [PCCP 모의고사 2] 3번
https://school.programmers.co.kr/learn/courses/15009/lessons/121689
"""

### input ########################
menu = [5, 12, 30]
order = [1, 2, 0, 1]
k = 10
###########################

from collections import deque

ans = 0
n = len(order)
q = deque()
i = 0
time = 0

while q or i <n:
    if not q:   # 큐가 비어 있다면
        time = (i*k) + menu[order[i]]   # 시간을 도착시간 + 주문시간 으로 변경
        i += 1
    else:   # 큐가 비어있지 않다면
        x = q.popleft()     # 큐에서 하나를 꺼내서
        time += menu[x]     # 시간에 주문 시간을 더함

    # while i < n and i <= ((time-1) // k):   # 입장한 사람이 있을 경우
    while i < n and i <= len(order) :
        q.append(order[i])  # 큐에 추가
        i += 1
    ans = max(ans, len(q))
# return (ans + 1)
print(ans)


## Tree 디버깅 시 사용######
root = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)