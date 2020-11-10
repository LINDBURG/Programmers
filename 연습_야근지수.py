import heapq as hq

class Night():
    def __init__(self, n, works):
        self.works = list(map(lambda x:-x, works))
        hq.heapify(self.works)
        self.run(n)
        
    def run(self, n):
        self.answer = 0
        for _ in range(n):
            num = hq.heappop(self.works)
            if num == 0:
                break
            hq.heappush(self.works, num+1)
        self.answer = 0
        for i in range(len(self.works)):
            self.answer += self.works[i]**2

def solution(n, works):
    night = Night(n, works)
    return night.answer