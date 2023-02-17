"""마구간 정하기(결정알고리즘)
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마구간 간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대값을 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

▣ 출력설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.

▣ 입력예제 1
5 3
1
2
8
4
9

▣ 출력예제 1
3

"""

def Count(len): # 말이 들어있는 마구간 갯수
    cnt = 1
    ep = horses[0]

    for i in range(1,n):
        if horses[i]-ep >= len:
            cnt += 1
            ep = horses[i]
    return cnt

n, c = map(int, input().split())

horses = []
res = 0
largest = 0

for _ in range(n):
    tmp = int(input())
    horses.append(tmp)

horses.sort()
lt = 1
rt = horses[n-1]

while lt<=rt:
    mid = (lt+rt)//2

    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)