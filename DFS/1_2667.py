"""
1. 아이디어
- 2중 for문, 값1 && 방문X => DFS
- DFS 를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간복잡도
- DFS: O(V+E)
- V, E: N^2, 4N^2
- V+E = 5N^2~=N^2 ~= 625 (가능

3. 자료구조
- 그래프 저장: int[][]
- 방문 여부: bool[][]
- 결과값: int[]

"""
import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]