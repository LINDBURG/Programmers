def solution(brown, red):
    answer = []
    row = 0
    col = 0
    flag =0

    rd = int(red ** 0.5) +1
    for div in range(2, rd):
        if red%div ==0:
            tc = div
            tr = red / tc
            if( (tc+tr)*2 + 4 ==brown):
                row = int(tr) + 2
                col = tc + 2
                flag = 1
                break
            
    if( flag ==0):
        col = 3
        row = red + 2

    answer = [row, col]
    print(answer)
    return answer



solution(8,1)
