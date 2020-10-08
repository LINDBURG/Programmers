class Numbers():
    def __init__(self, n):
        self.n = n
        self.to_three()
        self.to_ten()
        
    def to_three(self):
        res = ''
        while self.n:
            res = str(self.n%3) + res
            self.n = (self.n) // 3
        self.three = res
        
        
    def to_ten(self):
        res = 0
        for i in range(len(self.three)):
            res += int(self.three[i]) * (3**i)
        self.num = res
        
        

def solution(n):
    numbers = Numbers(n)
    return numbers.num