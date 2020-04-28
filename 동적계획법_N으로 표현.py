def solution(N, number):
    pos = [[0]] + [[int(str(N)*i)] for i in range(1,9)]
    for n in range(2,9):
        for i in range(1,n):
            for a in pos[i]:
                for b in pos[n-i]:
                    if a+b not in pos[n]:
                        pos[n].append(a+b)
                    if a*b not in pos[n]:
                        pos[n].append(a*b)
                    if a-b>0 and a-b not in pos[n]:
                        pos[n].append(a-b)
                    if b-a>0 and b-a not in pos[n]:
                        pos[n].append(b-a)
                    if b != 0 and a%b==0 and a//b not in pos[n]:
                        pos[n].append(a//b)
                    if a != 0 and b%a==0 and b//a not in pos[n]:
                        pos[n].append(b//a)
        if number in pos[n]:
            return n
    return -1
