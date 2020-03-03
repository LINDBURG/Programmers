def solution(routes):
    answer = 0
    routes.sort()

    while routes:
        answer += 1
        now = routes.pop(0)
        end = now[1]
        for i in range(len(routes)):
            if routes[i][1] < end:
                end = routes[i][1]
            elif routes[i][0] > end:
                break

        for route in routes[:]:
            if route[0] > end:
                break
            routes.pop(0)

    return answer
