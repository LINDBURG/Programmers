def solution(triangle):
    base = triangle[0]
    for i in range(1, len(triangle)):
        tmp = [triangle[i][0] + base[0]]
        for j in range(1, len(base)):
            tmp.append(max(base[j-1], base[j]) + triangle[i][j])
            
        tmp.append(triangle[i][-1] + base[-1])
        base = tmp
        
    return max(base)
