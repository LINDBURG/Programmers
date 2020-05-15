from itertools import combinations
import copy

def solution(relation):
    answer = []
    pool = [i for i in range(len(relation[0]))]
    cnt = 1
    while cnt <= len(pool):
        comb = list(combinations(pool,cnt))
        for ans in answer:
            for com in copy.deepcopy(comb):
                flag = 1
                for a in ans:
                    if a not in com:
                        flag = 0
                        break
                if flag == 1:
                    comb.remove(com)
        for com in comb:
            flag = 1
            for i in range(len(relation)):
                base = []
                for idx in com:
                    base.append(relation[i][idx])
                for j in range(i+1,len(relation)):
                    comp = []
                    for idx in com :
                        comp.append(relation[j][idx])
                    if base == comp:
                        flag = 0
                        break
                if flag == 0:
                    break
            if flag == 1:
                answer.append(com)
        cnt += 1
    return len(answer)
