class Islands():
    def __init__(self, costs):
        self.answer = 0
        self.tb = [i for i in range(100)]
        self.costs = sorted(costs, key = lambda x:x[2])
        self.run()
        
    def run(self):
        for i, j, cost in self.costs:
            res_i = self.tb[i]
            res_j = self.tb[j]
            if res_i != res_j:
                self.answer += cost
                new_tb = min(res_i, res_j)
                for k in range(100):
                    if self.tb[k] == res_i or self.tb[k] == res_j:
                        self.tb[k] = new_tb
                

def solution(n, costs):
    islands = Islands(costs)
    return islands.answer