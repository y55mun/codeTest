""" 벌집
https://www.acmicpc.net/problem/2292
"""

N = int(input())
nums = 1    # 초기 숫자 1의 벌집 갯수

for i in range(N):
    nums += i*6 # i번째 벌집 개수는 6의 배수로 늘어남. nums: 벌집 개수 누적

    if N <= nums:   # 벌집 개수의 누적이 입력값보다 커지면
        print(i+1)  # i+1 번째 겹 인것이므로 출력
        break