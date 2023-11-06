""" 다이얼
https://www.acmicpc.net/problem/5622
"""

# dic_time = {
#     '1': '2',
#     '2': ['3','A','B','C'],
#     '3': ['4','D','E','F'],
#     '4': ['5','G','H','I'],
#     '5': ['6','J','K','L'],
#     '6': ['7','M','N','O'],
#     '7': ['8','P','Q','R','S'],
#     '8': ['9','T','U','V'],
#     '9': ['10','W','X','Y','Z'],
#     '0': '11'
# }

# key: 걸린 시간, value: 다이얼 숫자
dic_time = {
    '2': '1',
    '3': ['2','A','B','C'],
    '4': ['3','D','E','F'],
    '5': ['4','G','H','I'],
    '6': ['5','J','K','L'],
    '7': ['6','M','N','O'],
    '8': ['7','P','Q','R','S'],
    '9': ['8','T','U','V'],
    '10': ['9','W','X','Y','Z'],
    '11': '0'
}

voca = list(input())

ans = []
for key, value in dic_time.items():
    for i in range(len(voca)):
        if voca[i] in value:
            ans.append(int(key))

print(sum(ans))


