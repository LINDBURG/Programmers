class Islands:
    def __init__(self, n):
        self.cost = 0
        self.node = [10000 for i in range(n)]
        self.movable = [dict() for i in range(n)]
        
    def costs(self, costs):
        self.queue = [cost[0][0]]
        for i,j,cost in costs:
            self.movable[i][j] = cost
            self.movable[j][i] = cost
        

def solution(n, costs):
    answer = 0
    islands = Islands(n)
    islands.costs(costs)
    
    return answer