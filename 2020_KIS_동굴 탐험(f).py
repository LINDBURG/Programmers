class Graph():
    def __init__(self, n, path, order):
        self.tree = [Node(i) for i in range(n)]
        self.order = []
        
        for i,j in path:
            self.tree[i].connect_path(j)
            self.tree[j].connect_path(i)
        self.connect([], 0)
        
        for start, end in order:
            self.calc(start, end)
        
    def calc(self, start, end):
        s_parent = self.tree[start].parent
        e_parent = self.tree[end].parent
        arr = list(set(s_parent + e_parent)) + [end]
        self.order.append(arr)
        
        
    def connect(self, parent, idx):
        node = self.tree[idx]
        node.parent = parent
        if idx > 0:
            node.children.remove(parent[-1])
        for cid in node.children:
            #print("1", idx, node.value,cid)
            self.connect(node.parent + [node.value], cid)
            #print("2", idx, node.value)
            
        
class Node():
    def __init__(self, val):
        self.parent = []
        self.value = val
        self.children = []
        
    def connect_path(self, con):
        self.children.append(con)
    
    
def solution(n, path, order):
    answer = True
    graph = Graph(n, path, order)
    #print(graph.order)
    return answer