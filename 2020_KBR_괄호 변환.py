def change(p):
    l = 0
    r = 0
    flag = 1
    for c in p:
        if c =='(':
            l += 1
        else:
            r += 1
            
        if l <r:
            flag = 0
        if l == r:
            break
    
    u = p[:l+r]
    v = p[l+r:]
    if len(u) == len(p) and flag == 1:
        return p
    elif flag == 1:
        return u + change(v)
    else:
        s = "(" + change(v) + ")"
        for i in range(1,len(u)-1):
            if u[i] == '(':
                s += ')'
            else:
                s += '('
        return s

def solution(p):
    answer = change(p)
    return answer
