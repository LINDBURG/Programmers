def solution(stones, k):
    idx = stones.index(max(stones[:k]))
    answer = stones[idx]
    start = 0
    while(start + k < len(stones)+1):
        if start > idx and stones[start+k-1] < stones[idx]:
            idx = start
            for nidx in range(start+1,start+k):
                if stones[idx] <= stones[nidx]:
                    idx = nidx
        elif stones[start+k-1] >= stones[idx]:
            idx = start +k-1
        
        #print(start, idx)
        if answer > stones[idx]:
            answer = stones[idx]
        start += 1
    #print(answer)
    return answer
