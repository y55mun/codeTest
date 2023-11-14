""" 그룹 단어 체커
https://www.acmicpc.net/problem/1316
"""

n = int(input())
ans = n

for _ in range(n):
    voca = input()

    for j in range(0, len(voca) -1):
        if voca[j] == voca[j+1]:
            pass
        elif voca[j] in voca[j+1:]:
            ans -= 1
            break

print(ans)