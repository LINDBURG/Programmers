class Building():
    def __init__(self, n, k, beg, end):
        self.n = n
        self.k = k
        self.mini = [i+1 for i in range(n)]
        self.connected = [[] for i in range(n)]

        for i in range(k):
            self.connect(beg[i]-1, end[i]-1)

        self.answer = len(set(self.mini)) - 1


    def connect(self, start, end):
        self.connected[start].append(end)
        self.connected[end].append(start)
        tmp = min(self.mini[start], self.mini[end])

        self.minimize(start, tmp)
        self.minimize(end, tmp)

    def minimize(self, target, value):
        queue = [target]
        while queue:
            now = queue.pop(0)
            if self.mini[now] > value:
                self.mini[now] = value
            for nxt in self.connected[now]:
                if self.mini[nxt] > value:
                    queue.append(nxt)

def solution(n, k, beg, end):
    building = Building(n, k, beg, end)
    return building.answer