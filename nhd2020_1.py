def solution(n, delivery):
    answer = ''
    yes = []
    uncertain = []
    no = []
    
    for one, two , flag in delivery:
        if flag == 1:
            yes.append(one)
            yes.append(two)
        else:
            uncertain.append([one,two])
    
    yes = list(set(yes))
    
    for one,two in uncertain:
        if one in yes:
            no.append(two)
        elif two in yes:
            no.append(one)
    
    for num in range(1, n+1):
        if num in yes:
            answer += "O"
        elif num in no:
            answer += "X"
        else:
            answer += "?"
    return answer
