"""바둑이 승차(DFS)
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태울수가 없다.
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
둘째 줄부터 N마리 바둑이의 무게가 주어진다.

▣ 출력설명
첫 번째 줄에 가장 무거운 무게를 출력한다.

▣ 입력예제 1
259 5_문자열
81
58
42
33
61

▣ 출력예제 1
242

"""

def dfs(l, sum, tsum):  # l: 인덱스, sum: 부분집합의 합, tsum: 판단한 부분집합의 합
    global result

    # total-tsum: 앞으로 판단해야 할 바둑이들의 총 무게
    if sum+(total-tsum) < result:     # cut-edge 2번 조건
        return      # 밑으로 가지 뻗을 필요가 없음
    if sum > c:     # cut-edge 1번 조건
        return
    if l == n:  # 종착점. 부분집합 1개 완성
        if sum > result:
            result = sum
    else:
        dfs(l+1, sum+a[l], tsum+a[l])
        dfs(l+1, sum, tsum+a[l])



c, n = map(int, input().split())
a = [0] * n     # 바둑이 각각의 무게
result = -2147000000        # 가장 큰 값을 구해야 하니, 아주 작은 값으로 초기화
for i in range(n):
    a[i] = int(input())
total = sum(a)

dfs(0, 0, 0)
print(result)
