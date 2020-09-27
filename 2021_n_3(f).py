class Computer():
    def __init__(self, edges, n):
        self.computers = [Node() for _ in range(n)]
        for parent, child in edges:
            self.computers[parent].children.append(child)
        self.root = 0
        self.blockable = self.computers[self.root].children
        self.corrupted = 1
        self.calc_cost(self.root)

        while(self.blockable):
            self.chose()
            self.corrupted += len(self.blockable)
            self.make_blockable()

    def make_blockable(self):
        new_blockable = []
        for child in self.blockable:
            new_blockable.extend(self.computers[child].children)
        self.blockable = new_blockable


    def chose(self):
        max_cost = -1
        max_child = -1
        for child in self.blockable:
            cost = self.computers[child].cost + len(self.computers[child].children)
            if cost > max_cost:
                max_cost = cost
                max_child = child

        if max_child != -1:
            self.blockable.remove(max_child)

    def calc_cost(self, now):
        now = self.computers[now]
        for child in now.children:
            now.cost += self.calc_cost(child)

        return now.cost


class Node():
    def __init__(self):
        self.cost = 1
        self.children = []


def solution(n, edges):
    computer = Computer(edges, n)
    return computer.corrupted