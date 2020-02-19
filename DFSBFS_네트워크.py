def solution(n, computers):
    answer = 0
    cnt =0
    net = [0]*n
    for com, con in enumerate(computers):
        if(net[com]==0):
            answer += 1
            net[com] = answer
        for idx in range(n):
            if(con[idx] ==1 and net[idx] == 0):
                net[idx] = net[com]
            elif(con[idx] ==1 and net[idx] != net[com]):
                cng = net[idx]
                cnt += 1
                net[idx] = net[com]
                for i in range(n):
                    if(net[i] == cng):
                        net[i] = net[com]

    answer -= cnt
    return answer

solution(5, [[1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1]])
