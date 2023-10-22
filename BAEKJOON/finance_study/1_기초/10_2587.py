""" 대표값2
https://www.acmicpc.net/problem/2587
"""

# list_num = [list(map(int, input())) for _ in range(5)]  # [[1, 0], [4, 0], [3, 0], [6, 0], [3, 0]]
# list_num = [list(input()) for _ in range(5)]      # [['1', '0'], ['4', '0'], ['3', '0'], ['6', '0'], ['3', '0']]
list_num = [int(input()) for _ in range(5)]     # [10, 40, 30, 60, 30]

print(int(sum(list_num) / 5))   # 평균

# list_num.sort()
# print(list_num[2])

# 버블 정렬
# for i in range(len(list_num) -1):
#     for j in range(len(list_num) - i -1):
#         if list_num[j] > list_num[j+1]:
#             list_num[j], list_num[j+1] = list_num[j+1], list_num[j]


print(list_num[5//2])