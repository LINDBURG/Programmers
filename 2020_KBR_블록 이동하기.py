def solution(board):
    answer = len(board)**2*2
    sec = [[[answer,answer] for i in range(len(board))] for j in range(len(board))]
    sec[0][0] = [0,answer]
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(board)):
            for j in range(len(board)):
                #가로
                if j < len(board) -1 and board[i][j] == 0 and board[i][j+1] == 0:
                    if j > 0 and board[i][j-1] == 0 and sec[i][j][0] + 1 < sec[i][j-1][0]:
                        sec[i][j-1][0] = sec[i][j][0] + 1
                        flag = 1
                    if j < len(board) -2 and board[i][j+2] == 0 and sec[i][j][0] + 1 < sec[i][j+1][0]:
                        sec[i][j+1][0] = sec[i][j][0] + 1
                        flag = 1
                    if i > 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0:
                        if sec[i][j][0] + 1 < sec[i-1][j][0]:
                            sec[i-1][j][0] = sec[i][j][0] + 1
                            flag = 1
                        #회전
                        if sec[i][j][0] + 1 < sec[i-1][j][1]:
                            sec[i-1][j][1] = sec[i][j][0] + 1
                            flag = 1
                        if sec[i][j][0] + 1 < sec[i-1][j+1][1]:
                            sec[i-1][j+1][1] = sec[i][j][0] + 1
                            flag = 1
                    if i < len(board) -1 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                        if sec[i][j][0] + 1 < sec[i+1][j][0]:
                            sec[i+1][j][0] = sec[i][j][0] + 1
                            flag = 1
                        #회전
                        if sec[i][j][0] + 1 < sec[i][j][1]:
                            sec[i][j][1] = sec[i][j][0] + 1
                            flag = 1
                        if sec[i][j][0] + 1 < sec[i][j+1][1]:
                            sec[i][j+1][1] = sec[i][j][0] + 1
                            flag = 1
                
                #세로
                if i < len(board) - 1 and board[i][j] == 0 and board[i+1][j] == 0:
                    if j >0 and board[i][j-1] == 0 and board[i+1][j-1] == 0:
                        if sec[i][j][1] + 1 < sec[i][j-1][1]:
                            sec[i][j-1][1] = sec[i][j][1] + 1
                            flag = 1
                        #회전
                        if sec[i][j][1] + 1 < sec[i][j-1][0]:
                            sec[i][j-1][0] = sec[i][j][1] + 1
                            flag = 1
                        if sec[i][j][1] + 1 < sec[i+1][j-1][0]:
                            sec[i+1][j-1][0] = sec[i][j][1] + 1
                            flag = 1
                    if j < len(board) - 1 and board[i][j+1] == 0 and board[i+1][j+1] == 0:
                        if sec[i][j][1] + 1 < sec[i][j+1][1]:
                            sec[i][j+1][1] = sec[i][j][1] + 1
                            flag = 1
                        #회전
                        if sec[i][j][1] + 1 < sec[i][j][0]:
                            sec[i][j][0] = sec[i][j][1] + 1
                            flag = 1
                        if sec[i][j][1] + 1 < sec[i+1][j][0]:
                            sec[i+1][j][0] = sec[i][j][1] + 1
                            flag = 1
                    if i > 0 and board[i-1][j] == 0 and sec[i][j][1] + 1 < sec[i-1][j][1]:
                        sec[i-1][j][1] = sec[i][j][1] + 1
                        flag = 1
                    if i < len(board) - 2 and board[i+2][j] == 0 and sec[i][j][1] + 1 < sec[i+1][j][1]:
                        sec[i+1][j][1] = sec[i][j][1] + 1
                        flag = 1
                    
                    
    
    return min(sec[len(board)-1][len(board)-2][0], sec[len(board)-2][len(board)-1][1])
