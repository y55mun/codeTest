""" 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""

from collections import deque

def solution(tickets):
    answer = deque()
    ticket_dict = {}

    for s, d in tickets:
        if s not in ticket_dict.keys():
            ticket_dict[s] = [d]
        else:
            ticket_dict[s].append(d)

    keys = ticket_dict.keys()
    for i in keys:
        ticket_dict[i].sort(reverse=True)

    stack = ['ICN']
    while stack:
        dt = stack[-1]
        if dt not in keys:
            answer.appendleft(stack.pop())
        elif not ticket_dict[dt]:
            answer.appendleft(stack.pop())
        else:
            stack.append(ticket_dict[dt].pop())
    return list(answer)

    for i in range(len(tickets)):  # 가로
        for j in range(len(tickets[i])):
            print(tickets[i][0])

    return answer
