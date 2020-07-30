def solution(dartResult):
    answer = []
    num = 0
    
    for i in range(len(dartResult)):
        c = dartResult[i]
        if c == 'S':
            continue
        elif c == 'D':
            answer[-1] *= answer[-1]
        elif c == 'T':
            answer[-1] = answer[-1]**3
        elif c == '#':
            answer[-1] = -answer[-1]
        elif c == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        else:
            if c!= '0':
                num = int(c)
            else:
                num *= 10
            if i+1 < len(dartResult) and dartResult[i+1].isdigit():
                continue
            else:
                answer.append(num)
                num = 0
    
    return sum(answer)