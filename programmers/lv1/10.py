'''
현대-softeer
A+B
https://softeer.ai/practice/info.do?idx=1&eid=362&sw_prbl_sbms_sn=183008
'''

import sys
input = sys.stdin.readline

T= int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print('Case #'+str(i)+': '+str(a+b))