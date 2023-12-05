""" 좋은 단어
https://www.acmicpc.net/problem/3986
"""

n = int(input())
stack = []

ans = 0

for i in range(n):
    s = input().rstrip()


    # 로직: 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 비교
    # 다른 위치에 있는 글자를 찾고
    # 그 글자와 현재 위치 글자를 연결

    for j in range(len(stack)):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if not stack:
        ans += 1
print(ans)
