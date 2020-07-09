def solution(food_times, k):
    cnt = {}
    for time in food_times:
        if time in cnt:
            cnt[time] += 1
        else:
            cnt[time] = 1
    
    l = len(food_times)
    for a in range(1,100000001):
        if l == 0:
            return -1
        if k < l:
            break
        k -= l
        if a in cnt:
            l -= cnt[a]
    #print(a, k, l)
    tmp = 0
    for idx, time in enumerate(food_times):
        if time >= a:
            tmp += 1
        if tmp > k:
            return idx + 1
    return 0
    