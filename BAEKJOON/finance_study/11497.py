""" 통나무 건너뛰기
https://www.acmicpc.net/problem/11497
"""

t = int(input())    # 테스트 케이스

for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    ans = 0
    for j in range(2, n):
        ans = max(ans, abs(trees[j] - trees[j-2]))
    print(ans)