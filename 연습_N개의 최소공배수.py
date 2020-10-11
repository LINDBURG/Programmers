from functools import reduce

def lcm(a,b):
    base = 1
    last = max(a,b)**0.5
    q = 2
    while q <= last:
        if a%q ==0 and b%q == 0:
            base *= q
            a //= q
            b //= q
        else:
            q += 1
    
    return base * a * b

def solution(arr):
    answer = reduce(lcm, arr)
    return answer