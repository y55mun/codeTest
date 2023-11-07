""" 팰린드롬인지 확인하기
https://www.acmicpc.net/problem/10988
"""

voca = str(input())

ans = "1"
for i in range(len(voca)):
    print(voca[:(len(voca)//2)])
    # print(voca[-1::(len(voca)//2)+1])
    print(voca[-1:(len(voca)//2)-1:-1])


    if len(voca) // 2: # voca 길이가 홀수 이면
        if voca[:(len(voca)//2)] == voca[:(len(voca)//2):-1]:
            ans = "1"
        else:
            ans = "0"
    else:
        if voca[:(len(voca)//2)] == voca[-1:(len(voca)//2)-1:-1]:
            ans = "1"
        else:
            ans = "0"

print(ans)