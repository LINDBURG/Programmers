from functools import reduce

class Line():
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.id = [i for i in range(1,n+1)]
        self.base = reduce(lambda x,y:x*y, [i for i in range(1,n)])
        self.answer = []
        self.run()
        
    def run(self):
        for i in range(self.n, 0,-1):
            idx = (self.k-1) // self.base
            num = self.id.pop(idx)
            self.answer.append(num)
            self.k %= self.base
            if i == 1:
                break
            self.base //= (i-1)
            

def solution(n, k):
    line = Line(n, k)
    return line.answer