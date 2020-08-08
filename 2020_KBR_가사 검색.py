class trie:
    def __init__(self):
        self.next = dict()
        self.count = dict()
        
    def insert(self, word):
        now = self
        for c in word:
            if len(word) not in now.count:
                now.count[len(word)] = 0
            now.count[len(word)] += 1
            
            if c not in now.next:
                now.next[c] = trie()
            now = now.next[c]
            
        
    def find(self, word):
        now = self
        for c in word:
            if c == '?':
                if len(word) in now.count:
                    return now.count[len(word)]
                else:
                    return 0
            else:
                if c in now.next:
                    now = now.next[c]
                else:
                    return 0
                
    def show(self):
        print(self.next, self.count)

def solution(words, queries):
    answer = []
    front = trie()
    back = trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    
    #front.show()
    #back.show()
    
    for query in queries:
        if query[0] == '?':
            answer.append(back.find(query[::-1]))
        else:
            answer.append(front.find(query))
    return answer