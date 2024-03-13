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
    order_list.append(menu[order[i]])

    current.append(len(order_list))

    order_list[0] = order_list[0] - k

    while order_list and order_list[0] <= 0:
        if len(order_list) >= 2:
            order_list[1] += order_list[0]
        order_list.pop(0)

print(max(current))
