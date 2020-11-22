def solution(n):
    now = 1
    last = 0
    for _ in range(n-1):
        now,last = now+last, now
    return now % 1234567