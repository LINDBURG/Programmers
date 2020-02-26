def solution(operations):
    answer = [0,0]
    lst = []
    for op in operations:
        if op[0] == 'I':
            lst.append(int(op[2:]))
        elif lst:
            if op[2] == '-':
                mn = min(lst)
                lst.remove(mn)
            else:
                mx = max(lst)
                lst.remove(mx)
    if lst:
        answer = [max(lst), min(lst)]
    return answer
