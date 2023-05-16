import sys
input = sys.stdin.readline

n1 = int(input())
n2 = input()

for i in range(len(n2), 0, -1):
    print(n1 * int(n2[i-1]))

print(n1 * int(n2))