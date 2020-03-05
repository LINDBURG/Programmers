def solution(N):
    lst = [1,1]
    while len(lst) <=80:
        lst.append(lst[-1] + lst[-2])
    if N != 1:
        return 2 * lst[N-2] + 4 * lst[N-1]
    return 4
