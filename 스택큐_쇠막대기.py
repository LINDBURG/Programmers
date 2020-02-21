def solution(arrangement):
    answer = 0
    left = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            left += 1
            answer += 1
        else:
            left -= 1
            if arrangement[i-1] =='(':
                answer -= 1
                answer += left
    print(answer)
    return answer

solution("()(((()())(())()))(())")
