def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, cnt in enumerate(citations):
        if idx >= cnt:
            answer = cnt
            break
    return answer


solution([12,121])
