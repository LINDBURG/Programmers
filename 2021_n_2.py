class Pyramid():
    def __init__(self, blocks):
        self.blocks = blocks
        self.pyramid = [[-200 for i in range(j+1)] for j in range(len(blocks))]
        self.result = []
        self.calc()

    def calc(self):
        for x, [y,cost] in enumerate(self.blocks):
            self.pyramid[x][y] = cost
            self.side('right', x, y+1)
            self.side('left', x, y-1)

        for i in range(len(self.blocks)):
            for j in range(i+1):
                self.result.append(self.pyramid[i][j])

    def side(self, tp, x, y):
        if tp == 'right' and y < len(self.pyramid[x]):
            self.pyramid[x][y] = self.pyramid[x-1][y-1] - self.pyramid[x][y-1]
            self.side(tp, x, y+1)
        elif tp == 'left' and y > -1:
            self.pyramid[x][y] = self.pyramid[x-1][y] - self.pyramid[x][y+1]
            self.side(tp, x, y-1)


def solution(blocks):
    pyramid = Pyramid(blocks)
    return pyramid.result