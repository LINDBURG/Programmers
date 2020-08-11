class Board:
    def __init__(self, board):
        self.board = board
        self.upper = []
        self.cnt = 0
        last = [0 for i in range(len(board))]
        for i in range(len(board)):
            line = []
            for j in range(len(board)):
                if board[i][j] == 0:
                    line.append(last[j])
                else:
                    line.append(last[j] + 1)
            self.upper.append(line)
            last = line

    def count(self):
        board = self.board
        upper = self.upper
        for i in range(len(board)-1):
            for j in range(len(board)-1):
                if j < len(board)-2 and board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] != 0:
                    ###
                    ###
                    if board[i+1][j] == board[i][j] and board[i][j+1] == 0 and upper[i][j+1] == 0 and board[i][j+2] == 0 and upper[i][j+2] == 0:
                        #   #
                        #   ###
                        self.cnt += 1
                        self.remove_horizon(i,j)
                    elif board[i+1][j] == board[i][j+1] and board[i][j] == 0 and upper[i][j] == 0 and board[i][j+2] == 0 and upper[i][j+2] == 0:
                        #    #
                        #   ###
                        self.cnt += 1
                        self.remove_horizon(i,j)
                    elif board[i+1][j] == board[i][j+2] and board[i][j] == 0 and upper[i][j] == 0 and board[i][j+1] == 0 and upper[i][j+1] == 0:
                        #     #
                        #   ###
                        self.cnt += 1
                        self.remove_horizon(i,j)
                elif i < len(board)-2 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+2][j+1] != 0 and board[i][j+1] == 0 and upper[i][j+1] == 0 and board[i+1][j+1] == 0 and upper[i+1][j+1] == 0:
                    #
                    #
                    ##
                    self.cnt += 1
                    self.remove_vertical(i,j)
                elif i < len(board)-2 and board[i][j+1] == board[i+1][j+1] == board[i+2][j] == board[i+2][j+1] != 0 and board[i][j] == 0 and upper[i][j] == 0 and board[i+1][j] == 0 and upper[i+1][j] == 0:
                    #    #
                    #    #
                    #   ##
                    self.cnt += 1
                    self.remove_vertical(i,j)

    def remove_horizon(self, i, j):
        board = self.board
        upper = self.upper
        for k in range(i,i+2):
            for l in range(j, j+3):
                board[k][l] = 0
        if i > 0:
            last = upper[i-1]
        else:
            last = [0 for k in range(len(board))]

        for k in range(i,len(board)):
            line = []
            for j in range(len(board)):
                if board[k][j] == 0:
                    line.append(last[j])
                else:
                    line.append(last[j] + 1)
            self.upper[k] = line
            last = line

    def remove_vertical(self, i, j):
        board = self.board
        upper = self.upper
        for k in range(i,i+3):
            for l in range(j, j+2):
                board[k][l] = 0
        if i > 0:
            last = upper[i-1]
        else:
            last = [0 for k in range(len(board))]

        for k in range(i,len(board)):
            line = []
            for j in range(len(board)):
                if board[k][j] == 0:
                    line.append(last[j])
                else:
                    line.append(last[j] + 1)
            self.upper[k] = line
            last = line

def solution(board):
    b = Board(board)
    for i in range(10):
        b.count()
    return b.cnt