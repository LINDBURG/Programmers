def solution(total_sp, skills):
    answer = []
    up = {}
    down = {}
    pt = []
    queue = []
    for a,b in skills:
        if b not in up:
            up[b] = a
        if a not in down:
            down[a] = 0
            
    pt = [0 for i in range(len(up)+2)]
    for idx in range(1,len(pt)):
        if idx not in down:
            queue.append(idx)
            
    while queue:
        now = queue.pop(0)
        pt[now] += 1
        if now in up:
            queue.append(up[now])
            
    base = total_sp / sum(pt)
    pt.pop(0)
    answer = [base*i for i in pt]
    return answer
