from collections import defaultdict

class Diamond():
    def __init__(self, grid):
        self.grid = grid
        self.pool = [[1,1], [-1,-1], [-1,1], [1,-1]]
        self.cnt = defaultdict(int)
        self.max_n = 2
        self.cnt[1] = len(grid)*len(grid[0])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for x_d, y_d in self.pool:
                    while True:
                        '''if self.check(x,y, x_d, y_d, self.max_n):
                            self.max_n += 1
                            continue'''
                        break

        if self.max_n == 2 and self.cnt[2] == 0:
            self.max_n = 1
        self.answer = [self.max_n, self.cnt[self.max_n]]

    def check(self, x, y, x_d, y_d, size):
        num = self.grid[x][y]
        if x_d == 1 and y_d == 1 and x-2*(size-1) > 0 and y + size-1 < len(self.grid[0]):
            for j in range(y,y + size):
                for case in range(size):
                    if self.grid[x][y] != num:
                        return 0

        self.cnt[size] += 1
        return 1


def solution(grid):
    diamond = Diamond(grid)
    return diamond.answer