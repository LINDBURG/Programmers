def solution(stones, k):
    l = len(stones)
    mini = max(stones[l-k:])
    mxi = -1
    while mxi< l-k:
        nstone = stones[mxi+1:min(mxi+1+k, l)]
        
        mx = max(nstone)   
        mxi += 1 + nstone.index(mx)
        
        
        if mini > mx:
            mini = mx
    return mini
