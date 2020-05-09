def solution(gems):
    answer = [0,len(gems)]
    cnt = {gem:0 for gem in set(gems)}
    last = 0
    find = gems[0]
    for k in list(cnt.keys()):
        tmp = gems.index(k)
        if tmp > last:
            last = tmp
            find = k
    
    start = 0
    end = 0
    while start < len(gems) and end <len(gems):
        while cnt[find] == 0 and end < len(gems):
            cnt[gems[end]] += 1
            end += 1
        while cnt[gems[start]] > 1:
            cnt[gems[start]] -= 1
            start += 1

        if cnt[find] != 0 and answer[1] - answer[0] > end-1 - start:
            answer = [start+1,end]
        
        #print(start,end)
        #print(cnt, answer)
        find = gems[start]
        cnt[gems[start]] -= 1
        start += 1
    return answer
