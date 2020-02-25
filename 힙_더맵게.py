import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <2:
            answer = -1
            break
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        n = a + b*2
        heapq.heappush(scoville, n)
    return answer
