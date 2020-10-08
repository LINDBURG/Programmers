class Tree():
    def __init__(self, n, edges):
        self.edges = edges
        self.node = [Node() for _ in range(n+1)]
        for i, j in edges:
            self.node[i].child.append(j)
            self.node[j].child.append(i)
            
        self.search(1)
        
    def search(self, parent):
        now = self.node[parent]
        for child in now.child:
            self.node[child].child.remove(parent)
            self.node[child].depth = now.depth + 1
            self.search(child)

    
class Node():
    def __init__(self):
        self.parent = []
        self.child = []
        self.depth = 0

def solution(n, edges):
    answer = 1
    tree = Tree(n, edges)
    return answer