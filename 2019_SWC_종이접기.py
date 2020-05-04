def solution(n):
    answer = [0]
    while n>1:
        tmp = [0]
        for i in range(len(answer)):
            tmp.append(answer[i])
            tmp.append((i+1)%2)
        answer = tmp
        n -= 1
    return answer
