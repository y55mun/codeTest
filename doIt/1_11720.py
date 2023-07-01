'''숫자의 합 구하기
https://www.acmicpc.net/problem/11720
'''
n = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum += int(i)

print(sum)