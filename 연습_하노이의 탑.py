class Hanoi():
    def __init__(self, n):
        self.n = n
        self.answer = []
        self.run(n, 1, 3)
        
        
    def run(self, depth, now, nxt):
        if depth <1:
            return 0
        mid = 6-now-nxt
        
        self.run(depth-1, now, mid)
        self.answer.append([now,nxt])
        self.run(depth-1, mid, nxt)
        
        
            

def solution(n):
    hanoi = Hanoi(n)
    return hanoi.answer