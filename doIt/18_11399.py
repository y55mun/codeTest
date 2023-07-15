""" ATM
https://www.acmicpc.net/problem/11399
"""

n = int(input())
a = list(map(int, input().split()))
s = [0] * n # 합 배열: 각 사람이 인출을 완료하는데 필요한 시간을 저장

for i in range(1, n):
    insert_point = i
    insert_value = a[i]

    for j in range(i-1, -1, -1):    # 현재 범위에서 삽입 위치 찾기
        if a[j] < a[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):    # 삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기기
       a[j] = a[j-1]
    a[insert_point] = insert_value  # 삽입 위치에 현재 데이터 저장

s[0] = a[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]

sum = 0
for i in range(0, n):
    sum += s[i]

print(sum)
