lines = {"0":[0,0,1,1]}
answer = 0

def slope(line, n, m, k):
    global lines
    attr = lines[line]
    
    
    if len(line) < m and attr[1] < n-1:
        next_0 = 0
        next_1 = 0
        
        #next 0
        if attr[0] == 0 and attr[3]<k-1:
            lines[line+"0"] = [0,attr[1], attr[2]+1, attr[3]+1]
            slope(line+"0", n, m, k)
        elif attr[0] == 1 and attr[1] <n-2:
            lines[line+"0"] = [0,attr[1]+1, attr[2]+1, 1]
            slope(line+"0", n, m, k)

        #next 1
        if attr[0] == 1 and attr[3]<k-1:
            lines[line+"1"] = [0,attr[1], attr[2], attr[3]+1]
            slope(line+"1", n, m, k)
        elif attr[0] == 0 and attr[1] <n-2:
            lines[line+"1"] = [0,attr[1]+1, attr[2], 1]
            slope(line+"1", n, m, k)          
        
        
        return next_0 + next_1
        
    elif len(line) == m and attr[1] == n-1 and attr[2]*2 == m:
        answer += 1

def solution(n, m, k):
    global answer
    slope("0", n,  m, k)
    print(lines)
    print((answer*2) % 1000000007)

solution(3,8,4)
