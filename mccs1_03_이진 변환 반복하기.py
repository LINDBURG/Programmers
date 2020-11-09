def solution(s):
    time = 0
    removed = 0
    while s != '1':
        time += 1
        removed += s.count('0')
        s = bin(s.count('1'))[2:]
    return [time, removed]