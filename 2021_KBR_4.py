class Node():
    def __init__(self, n, s, a, b, fares):
        self.connected = [dict() for _ in range(n+1)]
        for start, end, cost in fares:
            self.connected[start][end] = cost
            self.connected[end][start] = cost
            
        self.from_s = [-1 for _ in range(n+1)]
        self.from_a = [-1 for _ in range(n+1)]
        self.from_b = [-1 for _ in range(n+1)]
        self.mini = -1
        
        self.bfs(self.from_s, s)
        self.bfs(self.from_a, a)
        self.bfs(self.from_b, b)
        
        for i in range(n+1):
            if self.from_s[i] != -1 and self.from_a[i] != -1 and self.from_b[i] != -1:
                s = self.from_s[i] + self.from_a[i] + self.from_b[i]
                if self.mini == -1 or s < self.mini:
                    self.mini = s
        
        
    def bfs(self, target, start):
        queue = [start]
        target[start] = 0
        while queue:
            now = queue.pop(0)
            for end, cost in self.connected[now].items():
                if target[end] == -1 or target[now] + cost < target[end]:
                    target[end] = target[now] + cost
                    queue.append(end)
            
        

def solution(n, s, a, b, fares):
    node = Node(n, s, a, b, fares)
    print(node.mini)
    return node.mini