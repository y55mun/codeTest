""" 통나무 건너뛰기
https://www.acmicpc.net/problem/11497

알고리즘
통나무의 높이를 크기 순서대로 정렬하여 가장 큰 통나무를 가운데에 둠
양 옆을 그 다음으로 큰 통나무로 채움
"""

t = int(input())    # 테스트 케이스

for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    ans = 0
    for j in range(2, n):
        # 높이 차를 가장 안나게 하려면 현재 통나무 인덱스의 다음다음번째 인덱스를 가져와야 함
        # 1씩 차이나게 하면 가장 끝에 있는 통나무들의 높이차가 커지기 때문에 인덱스의 차이를 2로 두는 것이 베스트
        ans = max(ans, abs(trees[j] - trees[j-1]))
    print(ans)