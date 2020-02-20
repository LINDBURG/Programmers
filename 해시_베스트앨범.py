import operator

def solution(genres, plays):
    answer = []
    cat = {}
    for i in range(len(plays)):
        if genres[i] not in cat:
            cat[genres[i]] = [ plays[i], [[plays[i] + (10000-i)/10000, i]] ]
        else:
            cat[genres[i]][0] += plays[i]
            cat[genres[i]][1].append([plays[i] + (10000-i)/10000, i])
            
    scat = sorted(cat.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(len(scat)):
        tmp = scat[i][1][1]
        tmp.sort(reverse = True)
        print(tmp)
        answer.append(tmp[0][1])
        if(len(tmp)>1):
            answer.append(tmp[1][1])
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
