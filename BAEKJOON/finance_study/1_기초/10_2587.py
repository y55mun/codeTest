""" 대표값2
https://www.acmicpc.net/problem/2587
"""

# list_num = [list(map(int, input())) for _ in range(5)]  # [[1, 0], [4, 0], [3, 0], [6, 0], [3, 0]]
# list_num = [list(input()) for _ in range(5)]      # [['1', '0'], ['4', '0'], ['3', '0'], ['6', '0'], ['3', '0']]
list_num = [int(input()) for _ in range(5)]     # [10, 40, 30, 60, 30]
# print(list_num)

# avg = list_num / 5
# print(avg)

print(int(sum(list_num) / 5))   # 평균

list_num.sort()
print(list_num[2])