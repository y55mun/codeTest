'''
# 추억 점수

'''

def solution(name, yearning, photo):
    ans = []
    name_dic = {n:y for n,y in zip(name, yearning)}

    ans2 = []

    for i in range(len(photo)):            # 세로 크기
        for j in range(len(photo[i])):     # 가로 크기(4)
            if photo[i][j] in name_dic.keys():    # 해당 key 값이 존재 하면
                ans.append(name_dic.get(photo[i][j]))
        ans2.append(sum(ans))
        ans.clear()
    return ans2