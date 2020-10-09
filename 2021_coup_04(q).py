class Plan():
    def __init__(self, dept, hub, dest, roads):
        self.roads = roads
        self.entry = dict()
        self.cities = []

        self.build()

        self.dept = self.entry[dept]
        self.hub = self.entry[hub]
        self.dest = self.entry[dest]

        self.check(self.dept, self.hub, 0)
        self.check(self.hub, self.dest, 1)

        self.answer = self.search(self.dept, self.hub, 0)
        if self.answer != 0:
            self.answer *= self.search(self.hub, self.dest, 1)

    def check(self, start, end, tp):
        queue = [end]
        while queue:
            now = queue.pop(0)
            self.cities[now].connected[tp] = 1
            for parent in self.cities[now].parent:
                if self.cities[parent].connected[tp] == 0:
                    queue.append(parent)


    def search(self, start, end, tp):
        count = 0
        queue = [start]
        while queue :
            now = queue.pop(0)
            if now == end:
                count += 1
            for child in self.cities[now].child:
                if self.cities[child].connected[tp] == 1:
                    queue.append(child)
        return count

    def build(self):
        for start, end in self.roads:
            if start not in self.entry:
                self.entry[start] = len(self.cities)
                self.cities.append(City(start))
            if end not in self.entry:
                self.entry[end] = len(self.cities)
                self.cities.append(City(end))

            self.cities[self.entry[end]].parent.append(self.entry[start])
            self.cities[self.entry[start]].child.append(self.entry[end])

class City():
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.child = []
        self.connected = [0,0]

def solution(depar, hub, dest, roads):
    plan = Plan(depar, hub, dest, roads)
    return plan.answer