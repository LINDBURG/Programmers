from itertools import combinations

class Convenient():
    def __init__(self, n, money):
        self.money = sorted(money)
        self.cnt = [1] + [0 for _ in range(n + self.money[-1])]
        
        self.run(n)
        self.answer = self.cnt[n]
        #print(self.cnt)
        
        
    def run(self, n):
        for cost in self.money:
            for i in range(n+1):
                self.cnt[i+cost] += self.cnt[i]
        

def solution(n, money):
    convenient = Convenient(n, money)
    return convenient.answer