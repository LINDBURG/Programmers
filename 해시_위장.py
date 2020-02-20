def solution(clothes):
    answer = 1
    cat = {}
    for comb in clothes:
        if(comb[1] not in cat):
            cat[comb[1]] = [comb[0]]
        else:
            cat[comb[1]].append(comb[0])
    print(cat)
    for val in cat.values():
        answer *= len(val)+1
    print(answer)
    return answer -1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
