import operator as op
from functools import reduce

def nCr(n,r):
    r = min(r,n-r)
    numerator = reduce(op.mul, range(n,n-r,-1),1)
    denominator = reduce(op.mul, range(1, r+1),1)
    return numerator // denominator

def solution(n, m, k):
    half = m//2
    b = n//2
    w = b
    if n%2 == 1:
        w += 1

    bk = half -b
    bn = half -b + 1 -(bk//k)
    br = b -1 -(bk//k)
    print(bn, br)

    wk = half -w
    wn = half -w + 1 -(wk//k)
    wr = w -1 - (wk//k)
    print(wn, wr)
    
    answer = nCr(bn, br) * nCr(wn, wr)
    print((answer*2) % 1000000007)

solution(3,8,4) #6
solution(10,6,5) #0
solution(2,10,4) #0
solution(50, 150, 20) #780361386
