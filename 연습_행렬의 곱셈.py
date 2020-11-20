def solution(arr1, arr2):
    answer = []
    for s1 in arr1:
        tmp = []
        for y in range(len(arr2[0])):
            sum = 0
            for i in range(len(s1)):
                sum += s1[i]*arr2[i][y]
            tmp.append(sum)
        answer.append(tmp)
    return answer