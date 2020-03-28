def solution(s):
    answer = []
    lst = []
    st = ''
    for c in s[1:-1]:
        if c=='{':
            tmp = []
        elif c=='}':
            tmp.append(int(st))
            lst.append(tmp)
        elif c==',' and tmp[-1] != int(st):
            tmp.append(int(st))
            st = ''
            continue
        else:
            st += c
    print(lst)
    lst.sort(key=len)
    return answer
