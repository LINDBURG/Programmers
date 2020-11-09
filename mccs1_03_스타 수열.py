class Series():
    def __init__(self, a):
        self.cnt = [0 for _ in range(len(a))]
        self.odd = [1 for _ in range(len(a))]
        self.last = [-2 for _ in range(len(a))]
        
        self.run(a)
        
    def run(self, a):
        self.odd[a[0]] = 0
        
        for i in range(len(a)):
            n = a[i]
            if i - self.last[n] > 2:
                self.cnt[n] += 1
                self.odd[n] = 1
            elif i - self.last[n] == 2:
                self.cnt[n] += 1
            elif self.odd[n] == 1:
                self.odd[n] = 0
                self.cnt[n] += 1
                
            self.last[n] = i
        
        if self.odd[n] == 0:
            self.cnt[n] -= 1
            
        self.answer = max(self.cnt)*2

def solution(a):
    series = Series(a)
    return series.answer