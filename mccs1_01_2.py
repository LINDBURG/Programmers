import sys
sys.setrecursionlimit(1000000)

class Triangle():
    def __init__(self,n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.cnt = 1
        self.answer = []
        self.ldown(0,0,n)
        for i in range(n):
            for j in range(i+1):
                self.answer.append(self.board[i][j])

    def ldown(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x+n):
            self.board[i][y] = self.cnt
            self.cnt += 1
        self.right(i,y+1,n-1)
        
    def right(self,x,y,n):
        if n < 1:
            return 0
        for j in range(y,y+n):
            self.board[x][j] = self.cnt
            self.cnt += 1
        self.lup(x-1,j-1,n-1)
        
    def lup(self,x,y,n):
        if n < 1:
            return 0
        for i in range(x,x-n,-1):
            self.board[i][y] = self.cnt
            y -= 1
            self.cnt += 1
        self.ldown(i+1,y+1,n-1)

def solution(n):
    triangle = Triangle(n)
    return triangle.answer