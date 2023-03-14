"""재귀함수를 이용한 이진수 출력
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
단 재귀함수를 이용
해서 출력해야 합니다.

▣ 입력설명
첫 번째 줄에 10진수 N(1<=N<=1,000)이 주어집니다.

▣ 출력설명
첫 번째 줄에 이진수를 출력하세요.

▣ 입력예제 11
11

▣ 출력예제 1
1011

"""
res = []
ans = ''

def toBinary(n):
    global ans

    if n // 2 == 1:     # 몫이 1이면
        # res.append(n // 2)
        res.append(n%2)     # 2로 나눴을 때의 나머지를 저장
        # print(res.pop())    # 무조건 0
        res.append(n // 2)
        while res:
            # ans = ''.join(map(str, res.pop()))
            # print(ans)
            print(res.pop(), end='')

    else:   # 몫이 1이 아니면
        # 그 나머지 저장
        res.append(n%2)
        # print("111::", res.pop())
        # print(res.pop())

        # 2로 나누고
        n = n // 2

        toBinary(n)

n = int(input())
toBinary(n)
