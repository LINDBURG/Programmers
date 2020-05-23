def solution(p):
    while True:
        p += 1
        lst = list(str(p))
        st = set(lst)
        if len(lst) == len(st):
            return p
