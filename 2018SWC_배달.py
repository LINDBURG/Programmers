def solution(N, road, K):
    answer = 0
    dist = [0] + [-1 for i in range(N-1)]
    nroad = []
    for a,b,c in road:
        if a < b:
            nroad.append([a-1,b-1,c])
        else:
            nroad.append([b-1,a-1,c])

    queue = [0]
    while len(queue)>0:
        now = queue.pop(0)
        for line in nroad:
            if now ==line[0] or now == line[1]:
                nxt = line[0] + line[1] - now
                if dist[now] !=-1 and (dist[now] + line[2] <dist[nxt] or dist[nxt] == -1):
                    dist[nxt] = dist[now] + line[2]
                    queue.append(nxt)
                elif dist[nxt] !=-1 and (dist[nxt] + line[2] <dist[now] or dist[now] == -1):
                    dist[now] = dist[nxt] + line[2]
                    queue.append(now)

    for d in dist:
        if d <=K:
            answer += 1
    return answer
