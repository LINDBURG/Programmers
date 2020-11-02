class Multiset():
    def __init__(self, n, s):
        self.n = n
        self.s = s
        
    def run(self):
        base = self.s//self.n
        if base == 0:
            return [-1]
        
        plus_len = self.s - base*self.n
        return [base for _ in range(self.n-plus_len)] + [base+1 for _ in range(plus_len)]

def solution(n, s):
    multiset = Multiset(n, s)
    answer = multiset.run()
    return answer