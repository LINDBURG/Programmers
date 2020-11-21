class Geograph():
    def __init__(self, land, height):
        self.land = land
        self.height = height
        self.queue = []
        self.nodes = [Node(i, land[i//len(land)][i % len(land)], len(land)) for i in range(len(land)**2)]
        self.answer = 0
        self.include = []
        
        self.run(height)
        
    def run(self, height):
        self.queue = []
        for idx in range(len(self.nodes)):
            num = self.nodes[idx].idx
            self.queue.append(idx)
            while self.queue:
                now = self.queue.pop()
                self.spread(now, num)
                
        for idx in range(len(self.nodes)):
            node = self.nodes[idx]
            if node.x < len(self.land)-1 and node.idx != self.nodes[idx+len(self.land)].idx:
                self.include.append((abs(node.height - self.nodes[idx+len(self.land)].height), node.idx, self.nodes[idx+len(self.land)].idx))
            if node.y < len(self.land)-1 and node.idx != self.nodes[idx+1].idx:
                self.include.append((abs(node.height - self.nodes[idx+1].height), node.idx, self.nodes[idx+1].idx))
        self.include.sort()
        print(self.include)
            
        
    def spread(self, idx, num):
        node = self.nodes[idx]
        node.idx = num
        if node.x > 0 and abs(node.height- self.nodes[idx-len(self.land)].height) <= self.height and node.idx != self.nodes[idx-len(self.land)].idx:
            self.queue.append(idx-len(self.land))
        if node.y > 0 and abs(node.height- self.nodes[idx-1].height) <= self.height and node.idx != self.nodes[idx-1].idx:
            self.queue.append(idx-1)
        if node.x < len(self.land)-1 and abs(node.height- self.nodes[idx+len(self.land)].height) <= self.height and node.idx != self.nodes[idx+len(self.land)].idx:
            self.queue.append(idx+len(self.land))
        if node.y < len(self.land)-1 and abs(node.height- self.nodes[idx+1].height) <= self.height and node.idx != self.nodes[idx+1].idx:
            self.queue.append(idx+1)

class Node():
    def __init__(self, idx, height, size):
        self.idx = idx
        self.height = height
        self.x = idx // size
        self.y = idx % size

def solution(land, height):
    geograph = Geograph(land, height)
    return geograph.answer


solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3)