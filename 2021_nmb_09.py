class Nrook():
    def __init__(self, n, rooks):
        self.n = n
        self.rooks = rooks
        self.answer = 0
        self.board = [[0 for j in range(2*i-1)] for i in range(1, n+1)]

        self.choose(0)

    def choose(self, row):
        if len(self.board) == row:
            if self.rooks == 0:
                self.answer += 1
            return 0
        for j in range(len(self.board[row])):
            if self.board[row][j] == 0:
                self.color(row, j, 1)
                self.choose(row+1)
                self.color(row, j, -1)
        if self.rooks > -1:
            self.choose(row+1)

    def color(self, x, y, value):
        self.rooks -= value
        if y % 2 == 0:
            for i in range(1, len(self.board)- x):
                self.board[x+i][y] += value
                self.board[x+i][y+1] += value

                self.board[x+i][y+i*2-1] += value
                self.board[x+i][y+i*2] += value

        else:
            for i in range(len(self.board)-x):
                self.board[x+i][y] += value
                self.board[x+i][y-1] += value

                self.board[x+i][y+i*2] += value
                self.board[x+i][y+i*2+1] += value

def solution(n, rooks):
    nrook = Nrook(n, rooks)
    return nrook.answer