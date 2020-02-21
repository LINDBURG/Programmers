def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        progresses = list(map(lambda x, y:x+y, progresses, speeds))
        for p in progresses:
            if p >= 100:
                cnt += 1
            else:
                break
        if cnt != 0:
            answer.append(cnt)
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]
    return answer

solution([93, 30, 55], [1,30,5])
