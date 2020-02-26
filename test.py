import heapq

def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)
    heapq.heapify(jobs)

    tmp = []
    while jobs or tmp:
        while jobs:
            if jobs[0][0] <= start:
                job = heapq.heappop(jobs)
                heapq.heappush(tmp, (job[1], job[0]))
            else:
                break

        if tmp:
            job = heapq.heappop(tmp)
            start += job[0]
            answer += start - job[1]
        else:
            start += 1

    return answer // length
