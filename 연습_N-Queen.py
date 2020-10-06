class Chess():
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.count = 0
        self.run(0)
        
    def run(self, row):
        if row == self.n:
            self.count += 1
            return 0
        
        for j in range(self.n):
            if self.board[row][j] == 0:
                self.fill(row, j, 1)
                self.run(row+1)
                self.fill(row, j, -1)
        
    def fill(self, x, y, num):
        for i in range(1, self.n - x):
            self.board[x+i][y] += num
            if y-i > -1:
                self.board[x+i][y-i] += num
            if y+i < self.n:
                self.board[x+i][y+i] += num

def solution(n):
    answer = 0
    chess = Chess(n)
    return chess.count