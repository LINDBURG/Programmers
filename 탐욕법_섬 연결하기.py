class Islands:
    def __init__(self):
        self.answer = 0
        self.node = [10000 for i in range(100)]
        self.movable = [dict() for i in range(100)]
        self.installed = [[] for i in range(100)]
        
    def costs(self, costs):
        for i,j,cost in costs:
            self.movable[i][j] = cost
            self.movable[j][i] = cost
        self.run(costs[0][0], 0)
        
    def run(self, idx, val):
        node = self.node
        node[idx] = val
        for key,val in self.movable[idx].items():
            if key not in self.installed[idx] and val + node[idx] < node[key]:
                self.installed[idx].append(key)
                self.installed[key].append(idx)
                self.answer += val
                self.run(key, val + node[idx])
            if key in self.installed[idx] and abs(node[idx] - node[key]) < val:
                self.installed[idx].remove(key)
                self.installed[key].remove(idx)
                self.answer -= val

def solution(n, costs):
    islands = Islands()
    islands.costs(costs)
    return islands.answer