def solution(s):
    answer = [len(s)]
    for l in range(1,len(s)//2 + 1):
        res = len(s)%l +l
        cut = s[:l]
        cnt = 1
        for idx in range(1,len(s)//l):
            nxt = s[idx*l:(idx+1)*l]
            #print(cut, nxt, cnt, res)
            if cut == nxt:
                cnt += 1
            elif cut != nxt:
                if cnt >1:
                    res += len(str(cnt))
                res += l
                cnt = 1
                cut = nxt
        
        if cnt >1:
            res += len(str(cnt))
        answer.append(res)
    #print(answer)
    return min(answer)
