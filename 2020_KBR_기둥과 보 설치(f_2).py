class Frame:
    def __init__(self, size):
        self.frame = [[[1,0] for k in range(size+3)]] + [[[0,0] for i in range(size+3)] for j in range(size+2)]
        self.installed = []
        
    def install(self, query):
        y, x, tp = query
        frame = self.frame
        if tp == 0:
            #기둥
            if frame[x][y][0] > 0 or frame[x][y][1] > 0:
                frame[x+1][y][0] += 1
                self.installed.append(query)
        else:
            #보
            if frame[x][y][0] > 0 or frame[x][y+1][0] > 0 or (frame[x][y][1] > 0 and frame[x][y+1][1] > 0):
                frame[x][y][1] += 1
                frame[x][y+1][1] += 1
                self.installed.append(query)
        
    def remove(self, query):
        y, x, tp = query
        frame = self.frame
        if tp == 0:
            #기둥
            if y > 0 and frame[x+1][y][1] == 1 and frame[x+1][y-1][0] == 0 and [y-1,x,1] in self.installed:
                return 0
            elif frame[x+1][y][1] == 1 and frame[x+1][y+1][0] == 0 and [y+1,x,1] in self.installed:
                return 0
            elif frame[x+1][y][1] == 0 and frame[x+2][y][0] == 1:
                return 0
            frame[x+1][y][0] -= 1
            self.installed.remove(query)
        else:
            #보
            if frame[x][y][0] == 0 and frame[x+1][y][0] == 1 and frame[x][y][1] == 1:
                return 0
            elif frame[x][y+1][0] == 0 and frame[x+1][y+1][0] == 1 and frame[x][y+1][1] == 1:
                return 0
            elif y > 0 and frame[x][y][1] == 2 and frame[x][y-1][0] == 0 and frame[x][y][0] == 0:
                return 0
            elif frame[x][y+1][1] == 2 and frame[x][y+1][0] == 0 and frame[x][y+2][0] == 0:
                return 0
            frame[x][y][1] -= 1
            frame[x][y+1][1] -= 1
            self.installed.remove(query)
        
    def handle(self, query):
        if query[3] == 0:
            self.remove(query[:3])
        else:
            self.install(query[:3])
            
    def show(self):
        self.installed.sort(key=lambda x:(x[0],x[1],x[2]))
        return self.installed

def solution(n, build_frame):
    frame = Frame(n)
    for query in build_frame:
        frame.handle(query)
    answer = frame.show()
    return answer