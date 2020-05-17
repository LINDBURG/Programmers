from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    dists = list(permutations(dist,len(dist)))
    for rot in range(len(weak)):
        for dist in dists:
            di = 0
            wi = 0
            while wi < len(weak) and di < len(dist):
                last = weak[wi] + dist[di]
                wi += 1
                while wi < len(weak) and di < len(dist):
                    if weak[wi] > last:
                        break
                    wi += 1
                di += 1
            #print(wi, di)
            if len(weak) <= wi and di < answer:
                answer = di
        
        weak.append(weak.pop(0)+n)
        
    if answer == len(dist)+1:
        return -1
    return answer
