class Tree():
    def __init__(self, arr):
        self.board = arr
        self.answer = [0,0]
        self.compress(0, 0, len(arr))
        
    def compress(self, x, y, size):
        if size == 1:
            self.answer[self.board[x][y]] += 1
            return 0
        
            
        flag = self.board[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if self.board[i][j] != self.board[x][y]:
                    flag = -1
                    break
                        
        if flag == -1:
            size //= 2
            for i, j in [[0,0], [1,0], [0,1], [1,1]]:
                base_x = x + i * size
                base_y = y + j * size
                self.compress(base_x, base_y, size)
        else:
            self.answer[flag] += 1

def solution(arr):
    tree = Tree(arr)
    return tree.answer