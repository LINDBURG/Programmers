from collections import defaultdict
import math

def solution(X, Y):
    cnt = defaultdict(int)
    
    max_i = ""
    for x, y in zip(X, Y):
        gcd = math.gcd(x,y)
        line = str(x//gcd) + '+' + str(y//gcd)
        cnt[line] += 1
        
        if max_i == -1 or cnt[line] > cnt[max_i]:
            max_i = line
    
    return cnt[max_i]