def solution(food_times, k):
    cnt = {}
    for time in food_times:
        if time in cnt:
            cnt[time] += 1
        else:
            cnt[time] = 1
    
    l = len(food_times)
    start = 0
    for a in sorted(list(cnt.keys())):
        if k < (a-start)*l:
            break
        k -= (a-start)*l
        start = a
        l -= cnt[a]
        if l < 1:
            return -1
            
    k %= l
    tmp = 0
    for idx, time in enumerate(food_times):
        if time >= a:
            tmp += 1
        if tmp > k:
            return idx + 1
    