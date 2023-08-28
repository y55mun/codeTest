""" 여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""

def solution(tickets):
    answer = []
    ticket_dict = {}    # 티켓 정보를 저장하는 딕셔너리

    for (start, end) in tickets:
        if start in ticket_dict:
            ticket_dict[start].append(end)
        else:
            ticket_dict[start] = [end]

    # 갈 수 있는 공항을 알파벳 역순으로 정렬
    for t in ticket_dict.keys():
        ticket_dict[t].sort(reverse=True)
        
    st = ["ICN"]
    while st:
        top = st[-1]
        
        # 스택 top을 start 로 하는 티켓이 없는 경우
        if (top not in ticket_dict) or (not ticket_dict[top]):
            answer.append(st.pop()) # top을 스택에서 꺼내서 answer 에 저장
        else:   # 스택 top 을 start 로 하는 티켓이 있는 경우
            st.append(ticket_dict[top].pop())

    return answer[::-1]