def solution(n):
    answer = 0
    while n > 0:
        cnt = 0
        while 2**(cnt+1) <= n:
            cnt += 1
        answer += 3**cnt
        n -= 2**cnt
    return answer
