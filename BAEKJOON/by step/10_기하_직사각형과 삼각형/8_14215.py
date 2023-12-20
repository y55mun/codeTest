""" 세 막대
https://www.acmicpc.net/problem/14215
"""

li = sorted(list(map(int, input().split())))    # 오름차순 정렬
ans = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(ans)