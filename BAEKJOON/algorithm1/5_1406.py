"""에디터
https://www.acmicpc.net/problem/1406
"""

str = list(input())
m = int(input())
cursor = len(str)

for _ in range(m):
    command = list(input().split())

    if command[0] == 'P':   # $라는 문자를 커서 왼쪽에 추가함
        str.insert(cursor, command[1])
        cursor += 1
    elif command[0] == 'L':     #커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        if cursor > 0:
            cursor -= 1
    elif command[0] == 'D': # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        if cursor < len(str):
            cursor += 1
    else:     # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        if cursor > 0:
            str.remove(str[cursor-1])
print(''.join(str))

