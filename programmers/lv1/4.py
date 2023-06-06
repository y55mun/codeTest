def solution(arr):
    answer = 0

    for i in range(len(arr)):
        answer = sum(arr) / len(arr)

    return answer