def solution(m, n, board):
    answer = 0
    for i in range(m):
        board.append(list(board.pop(0)))
    while True:
        rm = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    rm.update([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
        rm = sorted(list(rm))

        for (i,j) in rm:
            for k in range(i,0,-1):
                board[k][j] = board[k-1][j]
            board[0][j] = '-'
        if len(rm)==0:
            break
        else:
            answer += len(rm)
    return answer