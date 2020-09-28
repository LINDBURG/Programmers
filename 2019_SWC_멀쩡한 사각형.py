import math

def gcd(a, b):
    if a > b:
        a, b = b, a
    gcd = 1
    case = 2
    while case <= a**0.5:
        if a%case == 0 and b%case == 0:
            gcd *= case
            a = a// case
            b = b// case
        else:
            case += 1
    
    return gcd, a,b

def count(a, b):
    cnt = 0
    for i in range(a):
        cnt += math.ceil(b*(i+1)/a) - math.floor(b*i/a)
    
    return cnt

def solution(w,h):
    base = w*h
    g, w, h = gcd(w, h)
    cnt = g * count(w,h)
        
    return base - cnt