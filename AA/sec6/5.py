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
259 5
81
58
42
33
61

▣ 출력예제 1
242

"""
import sys

def dfs(w, e):
    # for _ in range(n):
    total = sum(w[:e+1])
# print(w[0])
# print(w[:e+1])
#     print(total)
    # return
    # if total == c:
    #     print('완성!!::', total)
    #     return
    # elif total < c:
    #     beforeTotal = total
    #     afterTotal = dfs(w, e+1)
    #     if afterTotal > c:
    #         print('완성222', beforeTotal)

    # elif total > c:
    #     e -= 1
    #     dfs(w,e)
    if total < c:

        print(total)
        ans.append(total)
        dfs(w, e + 1)
    elif total > c:
        # dfs(w, e-1)
        print(ans.pop())
        sys.exit(0)




c, n = list(map(int, input().split()))
w = [int(input()) for _ in range(n)]
ans = []

# 아래의 for 문 대신 위에 코딩으로 바꿨음
# for _ in range(n):
#     w.append(input())
w.sort(reverse=True)

dfs(w, 0)


"""
1. 입력 받은 값들을 내림차순 sort =>
2. 아래 처럼 더한 값들과 c를 비교.  
    1+2
    1+2+3
    1+2+3+4
3. 더한 값 < c => 그 다음 값을 더해봄
4. 더한 값 == c => 이 값 출력
5. 더한 값 > c -> 이 전 값 까지만 더하고 출력 
"""
