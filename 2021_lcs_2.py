class Cube():
    def __init__(self, map3d):
        self.map3d = []
        for z, height in enumerate(map3d):
            n_height = []
            for y, row in enumerate(height):
                n_row = []
                for x, col in enumerate(row):
                    if col == 'X':
                        n_row.append(-2)
                    elif col == 'S':
                        n_row.append(0)
                        self.s = [z,y,x]
                    else:
                        n_row.append(-1)
                        if col == 'E':
                            self.e = [z,y,x]
                n_height.append(n_row)
            self.map3d.append(n_height)

        self.queue = []
        self.queue.append(self.s)
        self.run()
        self.answer = self.map3d[self.e[0]][self.e[1]][self.e[2]]

    def run(self):
        while self.queue:
            z,y,x = self.queue.pop(0)
            nxt = self.map3d[z][y][x] + 1
            #print(z,y,x,nxt)
            if z > 0 and (self.map3d[z-1][y][x] == -1 or self.map3d[z-1][y][x] > nxt):
                self.map3d[z-1][y][x] = nxt
                self.queue.append([z-1,y,x])
            if z < len(self.map3d)-1 and (self.map3d[z+1][y][x] == -1 or self.map3d[z+1][y][x] > nxt):
                self.map3d[z+1][y][x] = nxt
                self.queue.append([z+1,y,x])
            if y > 0 and (self.map3d[z][y-1][x] == -1 or self.map3d[z][y-1][x] > nxt):
                self.map3d[z][y-1][x] = nxt
                self.queue.append([z,y-1,x])
            if y < len(self.map3d[0])-1 and (self.map3d[z][y+1][x] == -1 or self.map3d[z][y+1][x] > nxt):
                self.map3d[z][y+1][x] = nxt
                self.queue.append([z,y+1,x])
            if x > 0 and (self.map3d[z][y][x-1] == -1 or self.map3d[z][y][x-1] > nxt):
                self.map3d[z][y][x-1] = nxt
                self.queue.append([z,y,x-1])
            if x < len(self.map3d[0][0])-1 and (self.map3d[z][y][x+1] == -1 or self.map3d[z][y][x+1] > nxt):
                self.map3d[z][y][x+1] = nxt
                self.queue.append([z,y,x+1])



def solution(map3d):
    cube = Cube(map3d)
    return cube.answer