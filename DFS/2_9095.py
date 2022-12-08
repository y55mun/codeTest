""" 백준 9095: 1, 2, 3 더하기
* 풀이 날짜: 2022-12-09

1. 아이디어
재귀 형식으로 풀기

2. 시간복잡도


3. 자료구조


"""

def solve(n):
    global cnt
    global k
    for i in arr:
        res.append(i)
        if sum(res) == n:
            res.pop()
            cnt += 1
            break
        solve(n)
        res.pop()
    return cnt


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [1, 2, 3]
    res = []
    cnt = 0
    print(solve(n))