'''
현대-softeer
근무 시간

'''

import sys

result = 0

for _ in range(5):
    s, e = sys.stdin.readline().split()
    stime, smin = s.split(":")
    etime, emin = e.split(":")
    stime, smin, etime, emin = int(stime), int(smin), int(etime), int(emin)

    if emin < smin:
        etime -= 1
        emin += 60

    result += (etime - stime) * 60 + (emin - smin)

print(result)