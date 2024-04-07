"""
https://leetcode.com/problems/climbing-stairs/description/
"""

n = int(input())

def climbStairs(n):
    memo = [-1] * (n + 1)
    def dp(n):
        if n==0 or n== 1:
            return 1
        if memo[n] == -1:
            memo[n] = dp(n-1) + dp(n-2)
        return memo[n]
    return dp(n)

print(climbStairs(n))