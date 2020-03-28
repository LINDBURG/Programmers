answer = []
def mul(now, rest):
    global answer
    for i in rest[0]:
        if i not in now:
            nnow = now[:]
            nnow.append(i)
            nnow.sort()
            if len(rest) > 1:
                mul(nnow, rest[1:])
            elif nnow not in answer:
                answer.append(nnow)


def solution(user_id, banned_id):
    global answer
    cnt = []
    
    for bid in banned_id:
        tmp = []
        for uid in user_id:
            if len(uid) == len(bid):
                flag = 1
                for i in range(len(uid)):
                    if bid[i] != '*' and uid[i] != bid[i]:
                        flag = 0
                        break
                if flag == 1:
                    tmp.append(user_id.index(uid))
        cnt.append(tmp)
    mul([], cnt)
    return len(answer)
