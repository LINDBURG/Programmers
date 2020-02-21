def solution(priorities, location):
    answer = 0
    while priorities:
        mx = max(priorities)
        now = priorities[0]
        if now >= mx:
            answer += 1
            priorities.pop(0)
            if location ==0:
                break
            location -=1
        else:
            priorities.append(priorities.pop(0))
            location = (location + len(priorities) -1) % len(priorities)
    return answer

solution([1, 1, 9, 1, 1, 1], 0)
