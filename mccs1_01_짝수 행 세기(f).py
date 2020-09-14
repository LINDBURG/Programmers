class Arr():
    def __init__(self,board):
        self.answer = 0
        self.row_num = len(board)
        self.col_num = len(board[0])
        self.col_cnt = [0 for _ in range(self.col_num)]
        self.row_check = [True for _ in range(self.row_num)]
        for row in board:
            for idx in range(len(row)):
                if row[idx] == 1:
                    self.col_cnt[idx] += 1
        
        self.run(0)
                    
    def run(self,depth):
        if depth == self.col_num and all(self.row_check):
            self.answer += 1
            return 0
        for idx in range(self.row_num):
            return 0
        

def solution(a):
    arr = Arr(a)
    print(arr.col_cnt)
    return 0

[[0,1,0],[1,1,1],[1,1,0],[0,1,1]]	#6
[[1,0,0],[1,0,0]]	#0
[[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]	#72