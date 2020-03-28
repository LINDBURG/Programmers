def solution(board, moves):
    answer = 0
    x = len(board[0])
    y = len(board)
    basket = []
    
    for ci in moves:
        ci -= 1
        sel = 0
        for i in range(len(board)):
            if board[i][ci] == 0:
                continue
            else:
                sel = board[i][ci]
                board[i][ci] = 0
                break
        
        if sel == 0:
            continue
        basket.append(sel)
        
        if len(basket) >1 and basket[-1] == basket[-2]:
            answer += 2
            basket.pop()
            basket.pop()
        
    return answer
