"""이진트리 순회(깊이우선탐색)

"""

def dfs(v):
    if v>7:
        return
    else:   # 중위 순회 방식
        dfs(v*2)    # 왼쪽 노드 호출
        print(v, end=" ")
        dfs(v*2+1)  # 오른쪽 노드 호출

dfs(1)