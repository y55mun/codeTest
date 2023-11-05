''' 수들의 합 5_문자열
https://www.acmicpc.net/problem/2018
투포인터
'''

n = int(input())
s = 1
e = 1
cnt = 1
sum = 1

while e != n:
    if sum < n:
        e += 1
        sum += e
    elif sum > n:
        sum -= s
        s += 1
    else:
        e += 1
        sum += e
        cnt += 1
print(cnt)
