import heapq as hq

class Coin():
    def __init__(self, m, v):
        self.m = m
        self.v = v
        self.heap = [0 for _ in range(m)]
        hq.heapify(self.heap)

        for cost in self.v:
            self.give(cost)

        self.answer = hq.heappop(self.heap)

    def give(self, cost):
        now = hq.heappop(self.heap)
        now += cost
        hq.heappush(self.heap, now)



def solution( m, v):
    coin = Coin(m, v)
    return coin.answer