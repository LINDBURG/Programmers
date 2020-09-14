def solution(a):
    answer = 0
    l_max = 1000000001
    r_max = 1000000001
    check = [[l_max,r_max] for _ in range(len(a))]
    for idx in range(len(a)):
        if l_max > a[idx]:
            l_max = a[idx]
        check[idx][0] = l_max
    for idx in range(len(a)-1,-1,-1):
        if r_max > a[idx]:
            r_max = a[idx]
        check[idx][1] = r_max
        
    for idx in range(len(a)):
        if a[idx] <= check[idx][0] or a[idx] <= check[idx][1]:
            answer += 1
    return answer