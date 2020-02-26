def solution(n, lost, reserve):
    for l in lost[:]:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
    answer = n - len(lost)

    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
    return answer
