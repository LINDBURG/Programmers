def solution(dirs):
    answer = 0
    road = []
    now = [0,0]
    for ins in dirs:
        if ins =='U':
            nxt = [now[0],now[1]+1]
        elif ins =='D':
            nxt = [now[0],now[1]-1]
        elif ins =='R':
            nxt = [now[0]+1,now[1]]
        elif ins =='L':
            nxt = [now[0]-1,now[1]]
        
        if nxt[0]>5 or nxt[0] <-5 or nxt[1] >5 or nxt[1] <-5:
            continue
        else:
            if [now,nxt] not in road and [nxt,now] not in road:
                road.append([now,nxt])
                answer += 1
            now = nxt
    return answer
