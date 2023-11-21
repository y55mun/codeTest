""" 벌집
https://www.acmicpc.net/problem/2292
"""

N = int(input())
nums = 1    # 초기 숫자 1의 벌집 갯수

for i in range(N):
    nums += i*6 # i번째 벌집 개수는 6의 배수로 늘어남. nums: 벌집 개수 누적

    if N<nums:
        print(i+1)
        break