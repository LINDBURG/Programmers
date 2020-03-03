def solution(weight):
    weight.sort()
    mx = weight[0]

    for i in range(1,len(weight)):
        if mx < weight[i] and mx + 1 != weight[i]:
            return mx + 1
        mx += weight[i]
    return mx + 1
