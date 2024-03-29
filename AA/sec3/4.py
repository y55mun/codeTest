"""두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제 1
3
1 3 5_문자열
5_문자열
2 3 6 7 9

▣ 출력예제 1
1 2 3 3 5_문자열 6 7 9
"""

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

p1=p2=0
c = []

while p1 < n and p2<m:
    if n_list[p1] <= m_list[p2]:
        c.append(n_list[p1])
        p1 += 1
    else:
        c.append(m_list[p2])
        p2 += 1

if p1 < n:
    c = c + n_list[p1:]
if p2 < m:
    c = c + m_list[p2:]

for x in c:
    print(x, end= ' ')
