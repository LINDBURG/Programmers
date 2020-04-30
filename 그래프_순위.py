def solution(n, results):
    answer = 0
    wl = [[[],[]] for i in range(n+1)]
    for w,l in results:
        win = [w]
        lose = [l]
        i=0
        while i< len(win):
            now = win[i]
            i += 1
            for num in wl[now][0]:
                if num not in win:
                    win.append(num)
        i = 0
        while i<len(lose):
            now = lose[i]
            i+= 1
            for num in wl[now][1]:
                if num not in lose:
                    lose.append(num)
        for w in win:
            for l in lose:
                if l not in wl[w][1]:
                    wl[w][1].append(l)
                if w not in wl[l][0]:
                    wl[l][0].append(w)
        #print(win)
        #print(lose)
        #print(wl)
    for cnt in wl:
        if len(cnt[0]) + len(cnt[1]) ==n-1:
            answer += 1
    return answer
