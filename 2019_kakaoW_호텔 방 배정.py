def find(pool, want):
    cng = [want]
    while want in pool:
        want = pool[want]
        cng.append(want)
    nxt =want+1
    while nxt in pool:
        cng.append(nxt)
        nxt = pool[nxt]

    for num in cng:
        pool[num] = nxt
    
    return want
    

def solution(k, room_number):
    answer = []
    pool = {}
    for want in room_number:
        res = find(pool, want)
        answer.append(res)

    return answer

solution(10,[1,3,4,1,3,1])
