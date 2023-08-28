""" 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""

def solution(tickets):
    answer = []
    ticket_dict = {}

    for (start, end) in tickets:
        if start in ticket_dict:
            ticket_dict[start].append(end)
        else:
            ticket_dict[start] = [end]

    for t in ticket_dict.keys():
        ticket_dict[t].sort(reverse=True)
    st = ["ICN"]
    while st:
        top = st[-1]
        if (top not in ticket_dict) or (not ticket_dict[top]):
            answer.append(st.pop())
        else:
            st.append(ticket_dict[top].pop())

    return answer[::-1]