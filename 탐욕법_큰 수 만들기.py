def solution(number, k):
    answer = ""
    number = list(number)

    start = 0
    while k > 0:
        mxi = start
        if start + k == len(number):
            break
        for i in range(start, start + k + 1):
            if number[mxi] < number[i]:
                mxi = i
            if number[mxi] == '9':
                break
        k -= mxi - start
        start = mxi +1
        answer += number[mxi]
    for i in range(start, len(number) - k):
        answer += number[i]
    return answer

solution("999991", 1)
