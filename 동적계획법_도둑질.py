def solution(money):
    answer = 0
    maxi = [[0,money[0]], [money[1],0],[money[2],money[0]+money[2]]]

    for i in range(3,len(money)):
        maxi.append([max(maxi[i-3][0],maxi[i-2][0])+money[i],max(maxi[i-3][1],maxi[-2][1])+money[i]])

    return max(maxi[-3][0], maxi[-3][1], maxi[-2][0], maxi[-2][1], maxi[-1][0], maxi[-1][1]-money[0])
