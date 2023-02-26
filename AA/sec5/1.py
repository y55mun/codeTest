"""가장 큰 수
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.

▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명
가장 큰 수를 출력합니다.

▣ 입력예제 1
5276823 3

▣ 출력예제 1
7823

▣ 입력예제 2
9977252641 5

▣ 출력예제 2
99776

"""

num, m = map(int, input().split())

stack = []
num = list(map(int, str(num)))      # list , string 화 시킴

for x in num:
    # 비어 있거나, m개 모두 제거 했거나, 마지막 수가 x 보다 작을 때
    # 값을 꺼냄
    while stack and m>0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

# m개를 다 지우지 못했을 경우
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))

print(res)