from collections import defaultdict

def solution(A):
    cnt = defaultdict(int)
    
    max_n = -1
    answer = 0
    for n in A:
        if cnt[n] > 1:
            continue
        answer += 1
        cnt[n] += 1
        if max_n == -1 or n > max_n:
            max_n = n
    if cnt[max_n] == 2:
        answer -= 1
    return answer
