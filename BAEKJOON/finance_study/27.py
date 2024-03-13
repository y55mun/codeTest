""" [PCCP 모의고사 2] 3번
https://school.programmers.co.kr/learn/courses/15009/lessons/121689
"""

### input ########################
menu = [5, 12, 30]
order = [1, 2, 0, 1]
k = 10
###########################


order_list = []
current = []

for i in range(len(order)):
    order_list.append(menu[order[i]])   # 주문 리스트 추가

    current.append(len(order_list)) # 현재의 주문수를 리스트에 추가

    order_list[0] = order_list[0] - k   # 제일 앞 손님의 음료 제조 시간 차감
    
    # 차감 결과가 음수 라면 바로 다음 주문의 제조 시간 차감
    # 음수가 된 주문 리스트에서 제거하여 다음 손님이 제일 앞 손님이 됨
    while order_list and order_list[0] <= 0:
        if len(order_list) >= 2:
            order_list[1] += order_list[0]
        order_list.pop(0)

print(max(current)) # 주문 수 목록에서 제일 큰 수 리턴
