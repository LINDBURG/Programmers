class Board():
    def __init__(self, n, ladder):
        self.n = n
        self.ladder = ladder
        self.answer = [i+1 for i in range(n)]
        for row in range(len(self.ladder)-1,-1,-1):
            self.change(row)
            #print(self.answer)

    def change(self, row):
        for i in range(self.n-1):
            if self.ladder[row][i] == 1:
                self.answer[i], self.answer[i+1] = self.answer[i+1], self.answer[i]

def solution(n, ladder):
    board = Board(n, ladder)
    return board.answer