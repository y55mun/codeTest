""" 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095


f(1) = 1
f(2) = (1)+1 = 2
f(3) =  1+1+1
        1+2  => 3
        2+1

f(4) = 7
1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1

"""
t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0] * (n+1)

    for i in range(1, n+1):
        if n==1:
            print(1)
        elif n==2:
            print(2)
        elif n==3:
            print(4)
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
