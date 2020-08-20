import sys
sys.setrecursionlimit(1000000)

class Graph():
    def __init__(self, n, path, order):
        self.tree = [Node(i) for i in range(n)]
        self.order = []
        self.flag = True

        for i,j in path:
            self.tree[i].connect_path(j)
            self.tree[j].connect_path(i)
        self.connect([], 0)

        for start, end in order:
            #self.calc(start, end)
            self.tree[start].children.append(end)

        self.answer(0, 0)

    '''def calc(self, start, end):
        s_parent = self.tree[start].parent
        e_parent = self.tree[end].parent
        arr = list(set(s_parent + e_parent)) + [end]
        self.order.append(arr)'''


    def connect(self, parent, idx):
        node = self.tree[idx]
        node.parent = parent
        if idx > 0:
            node.children.remove(parent[-1])
        for cid in node.children:
            #print("1", idx, node.value,cid)
            self.connect(node.parent + [node.value], cid)
            #print("2", idx, node.value)

    def answer(self, idx, counter):
        node = self.tree[idx]
        if self.flag == False:
            return 0

        node.discovered = counter

        for cid in node.children:
            cnode = self.tree[cid]
            if cnode.discovered == -1:
                self.answer(cid, counter + 1)
            elif node.discovered < cnode.discovered:
                continue
            elif cnode.finished == -1:
                self.flag = False
                return 0

        node.finished = 1


class Node():
    def __init__(self, val):
        self.parent = []
        self.value = val
        self.children = []
        self.discovered = -1
        self.finished = -1

    def connect_path(self, con):
        self.children.append(con)


def solution(n, path, order):
    graph = Graph(n, path, order)
    #print(graph.order)
    return graph.flag