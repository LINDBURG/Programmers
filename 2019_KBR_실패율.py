def solution(N, stages):
    answer = []
    cnt = [0 for i in range(N+2)]
    for stage in stages:
        cnt[stage] += 1
    accu = cnt[:]
    for i in range(N,0,-1):
        accu[i] = accu[i+1] + cnt[i]
        
    rate = []
    for i in range(1,N+1):
        if accu[i] == 0:
            r = 0
        else:
            r = cnt[i]/accu[i]
        rate.append([i,r])
        
    rate.sort(key=lambda x:(-x[1],x[0]))
    
    for idx,r in rate:
        answer.append(idx)
    return answer
