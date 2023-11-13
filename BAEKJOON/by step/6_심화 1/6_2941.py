''' 크로아티아 알파벳
https://www.acmicpc.net/problem/2941
'''

cro = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
voca = input()

for i in cro:
    voca = voca.replace(i, '*') # cro 에 동일한 문자열이 있으면 * 기호로 변환

print(len(voca))