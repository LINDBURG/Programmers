def solution(m, n, puddles):
    tmp = [0] * n
    route = []
    for i in range(m):
        route.append(tmp[:])
    route[0][0] = 1
    for i in range(m):
        for j in range(n):
            if [i+1,j+1] in puddles or (i == 0 and j == 0):
                continue
            
            if i != 0 and j != 0:
                route[i][j] = route[i-1][j] + route[i][j-1]
            elif i == 0:
                route[i][j] = route[i][j-1]
            elif j == 0:
                route[i][j] = route[i-1][j]
    return route[-1][-1] % 1000000007
