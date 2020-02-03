from itertools import permutations

def solution(baseball):
    answer = 0

    arr = possible(baseball[0])

    for i in range(1, len(baseball)):
        arr = list(set(arr) & set(possible(baseball[i])))

    answer = len(arr)
    
    return answer

def possible(arr):
    base = []
    num = str(arr[0])
    s = arr[1]
    b = arr[2]

    status = []
    for i in range(s):
        status.append("s")
    for i in range(b):
        status.append("b")
    for i in range(3-s-b):
        status.append("n")

    status = list(set(map(''.join, permutations(status))))
    for stat in status:
        pool = []
        for i in range(3):
            pool.append(list(range(1,10)))

        ball = []
        for idx in range(len(stat)):
            if stat[idx] == "s":
                for i in range(3):
                    if(int(num[idx]) in pool[i]):
                        pool[i].remove(int(num[idx]))
                pool[idx] = [int(num[idx])]
            elif stat[idx] =="b":
                if(int(num[idx]) in pool[idx]):
                    pool[idx].remove(int(num[idx]))
                ball.append(int(num[idx]))
            else:
                for i in range(3):
                    if(int(num[idx]) in pool[i]):
                        pool[i].remove(int(num[idx]))
            
        for a in pool[0]:
            for b in pool[1]:
                for c in pool[2]:
                    tmp = str(a) + str(b) + str(c)
                    flag = 1
                    for m in ball:
                        if(not(str(m) in tmp)):
                            flag = 0
                            break
                    if( flag ==1 and a!=b and a!=c and b!=c):
                        base.append(tmp)

    return base
        
        



data = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

solution(data)
