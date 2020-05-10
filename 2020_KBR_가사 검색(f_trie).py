def check(parent,query):
    #print(parent,query)
    if len(query) == 0 and '/' in parent:
        #print("ok")
        return 1
    elif len(query) == 0:
        return 0
    cnt = 0
    c = query[0]
    query = query[1:]
    if c =="?":
        for value in list(parent.values()):
            cnt += check(value,query)
    elif c in parent:
        cnt += check(parent[c],query)
    return cnt

def solution(words, queries):
    answer = []
    f_words = {}
    b_words = {}
    q_words = {}
    for word in words:
        if len(word) not in q_words:
            q_words[len(word)] = 1
            f_words[len(word)] = {}
            b_words[len(word)] = {}
        else:
            q_words[len(word)] += 1
        
        parent = f_words[len(word)]
        for c in word:
            if c not in parent:
                parent[c] = {}
            parent = parent[c]
        parent['/'] = {}
        
        word = word[::-1]
        parent = b_words[len(word)]
        for c in word:
            if c not in parent:
                parent[c] = {}
            parent = parent[c]
        parent['/'] = {}
        
    for query in queries:
        if len(query) not in q_words:
            answer.append(0)            
        elif query[0] == "?" and query[-1] == "?":
            answer.append(q_words[len(query)])
        elif query[-1] == "?":
            answer.append(check(f_words[len(query)], query))
        elif query[0] == "?":
            answer.append(check(b_words[len(query)], query[::-1]))
            
    return answer

