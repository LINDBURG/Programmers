def solution(K, travel):
    answer = [(0,0)]
    for wt, wm, bt,bm in travel:
        tmp = {}
        for m,t in answer:
            if t + wt <= K and ((m+wm) not in tmp or (tmp[m+wm] > t + wt)):
                tmp[m+wm] = t + wt
            if t + bt <= K and ((m+bm) not in tmp or (tmp[m+bm] > t + bt)):
                tmp[m+bm] = t + bt
        answer = list(tmp.items())
    
    mx = answer[0][0]
    for m,t in answer:
        if m > mx:
            mx = m
    return mx
