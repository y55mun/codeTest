""" 디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627

로직 설명
현재 시점에서 처리할 수 있는 작업들을 힙에 넣고, 하나를 뽑아 현재 시점과 총 대기 시간을 구해주는 것을 모든 작업을 처리할 때까지 반복한다.

힙에 push 할 때는 "작업의 소요 시간"을 기준으로 최소힙이 만들어져야 하기 때문에 jobs 의 요소들을 그대로 넣지 않고 [작업의 소요 시간, 작업이 요청되는 시점] 으로 요소의 앞뒤를 바꿔서 넣어준다.

1) 현재 시점에서 처리할 수 있는 작업인지 판별하는 조건
바로 이전에 완료한 작업의 시작 시간(start)<= 작업의 요청 시간 <= 현재 시점(now)

2) 처리할 수 있는 작업이 없을 경우
남아 있는 작업들의 요청 시간이 아직 오지 않은 것 이기 때문에 현재 시점(now) + 1

"""
import heapq

def solutions(jobs):
    ans, now, i = 0, 0, 0   # 작업하는데 걸린 총 시간, 현재 시간, 처리된 작업의 개수
    heap = []   # 현재 처리 가능한 jobs을 담는 힙
    start = -1  # 이전에 완료한 작업의 시작 시간

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now: # 이전에 끝낸 작업보다 큰 시간이고, 현재 시점보다 작은 시간인 경우에만 작업 가능
                heapq.heappush(heap, [j[1], j[0]])  # (처리시간, 요청 시간)

        if len(heap) > 0:   # 힙에 처리할 작업이 남아 있을 경우
            current = heapq.heappop(heap)   # 현재 처리중인 작업
            start = now
            now += current[0]
            ans += (now-current[1]) # 작업 요청 시간부터 처리 완료 까지의 시간 계산
            i += 1
        else:   # 처리할 작업이 없는 경우
            now += 1

    ans = ans // len(jobs)  # 평균 처리 시간 계산
    return ans

# jobs = [[0, 3], [1, 9], [2, 6]]     #  [작업이 요청되는 시점, 작업의 소요시간]
# print(solutions(jobs))