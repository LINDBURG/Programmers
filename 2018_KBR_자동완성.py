class node:
    def __init__(self):
        self.trie = dict()
        
    def insert(self, line):
        now = self.trie
        for c in line:
            if c not in now:
                now[c] = [1,dict()]
            else:
                now[c][0] += 1
            now = now[c][1]
            
    def show(self):
        print(self.trie)
        
    def find(self, line):
        depth = 1
        now = self.trie
        for c in line[:-1]:
            if now[c][0] == 1:
                break
            now = now[c][1]
            depth += 1
        
        #print(line, depth)
        return depth

def solution(words):
    answer = 0
    n = node()
    for word in words:
        n.insert(word)
    #n.show()
    for word in words:
        answer += n.find(word)
    return answer