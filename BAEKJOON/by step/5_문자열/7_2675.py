""" 문자열 반복
https://www.acmicpc.net/problem/2675
"""

T = int(input())

for i in range(T):
    R, S = input().split()  # 맨 처음에 숫자 문자 따로 받으려고 해서 헷갈렸었음..ㅠㅠ

    R = int(R)
    S = str(S)

    for i in range(len(S)):
        print(S[i] * R, end='')
    print()