"""
https://school.programmers.co.kr/learn/courses/15008/lessons/121685
"""

queries = list(map(int, input().split()))
ans = []
beans ={1: "RR", 2:"Rr", 3: "Rr", 4:"rr"}

def find(n,p):
    beans

    if n <= 2:
        ans = beans[p]
        return ans
    N = 4**(n-2)
    if p <= N:
        ans = "RR"
    elif p <= 2*N:
        ans = find(n-1, p-N)
    elif p <= 3*N:
        ans = find(n-1, p-2*N)
    else:
        ans = "rr"
    return ans

for n, p in queries:
    ans = find(n,p) if n>1 else "Rr"
    ans.append(ans)

print(ans)