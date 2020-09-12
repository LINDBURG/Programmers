class Tree():
    def __init__(self,infos, queries):
        self.infos = [info.split() for info in infos]
        self.queries = [query.replace(' and ',' ').split() for query in queries]
        self.result = []
        self.cnt = 0
        self.root = Node(0)
        
        for info in self.infos:
            self.add_child(self.root, info[:-1], int(info[-1]))
            
        #for query in self.queries:
            self.cnt = 0
            #self.search(self.root, query[:-1], int(query[-1]))
            self.result.append(self.cnt)
        
    def add_child(self,parent, children, score):
        if not children:
            parent.score.append(score)
            return 0
        
        value = children.pop(0)
        child = parent.children[value]
        self.add_child(child, children, score)
        
    def search(self, parent, children, score):
        if not children:
            if parent.visited == 0:
                parent.visited = 1
                parent.score.sort()
            for data in parent.score[::-1]:
                if data >= score:
                    self.cnt += 1
                else:
                    break
            return 0
        
        value = children.pop(0)
        if value == '-':
            for child in parent.children.values():
                self.search(child, children[:], score)
        else:
            child = parent.children[value]
            self.search(child, children, score)
        
        
        
class Node():
    def __init__(self, depth):
        self.score = []
        self.children = dict()
        self.visited = 0
        if depth == 0:
            self.children['java'] = Node(depth + 1)
            self.children['python'] = Node(depth + 1)
            self.children['cpp'] = Node(depth + 1)
        elif depth == 1:
            self.children['backend'] = Node(depth + 1)
            self.children['frontend'] = Node(depth + 1)
        elif depth == 2:
            self.children['junior'] = Node(depth + 1)
            self.children['senior'] = Node(depth + 1)
        elif depth == 3:
            self.children['chicken'] = Node(depth + 1)
            self.children['pizza'] = Node(depth + 1)
        
        

def solution(info, query):
    tree = Tree(info, query)
    #print(tree.root.children['python'].children['frontend'].children['senior'].children['chicken'].score)
    return tree.result