"""동전 0
- 참고: https://www.acmicpc.net/problem/11047

1. 아이디어
- 동전을 저장한 뒤, 반대로 뒤집음
- 동전 for >
    - 동전 사용 갯수 추가
    - 동전 사용한 만큼 k값 갱신

2. 시간복잡도
- O(N)

3. 자료구조
- 동전 금액: int[]
- 동전 사용 cnt: int
- 남은 금액: int
"""
