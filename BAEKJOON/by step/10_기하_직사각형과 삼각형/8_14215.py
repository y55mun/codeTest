""" 세 막대
https://www.acmicpc.net/problem/14215
"""

li = sorted(list(map(int, input().split())))    # 오름차순 정렬

# 삼각형의 조건: 가장 큰 값 < 다른 두 값의 합
# 가장 큰 값을 조절할 때는 최소한으로 조절해야 함 -> 다른 두 숫자의 합-1

ans = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(ans)