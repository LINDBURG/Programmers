def solution(words, queries):
    answer = []
    f_words = {}
    b_words = {}
    q_words = {}
    for word in words:
        if len(word) not in q_words:
            q_words[len(word)] = 1
        else:
            q_words[len(word)] += 1
        
        for i in range(1,len(word)):
            n_word = word[:i] + "?"*(len(word)-i)
            if n_word not in f_words:
                f_words[n_word] = 1
            else:
                f_words[n_word] += 1
            
            n_word = word[:i-1:-1] + "?"*i
            if n_word not in b_words:
                b_words[n_word] = 1
            else:
                b_words[n_word] += 1
    
    for query in queries:
        if query[0] == "?" and query[-1] == "?" and len(query) in q_words:
            answer.append(q_words[len(query)])
        elif query[-1] == "?" and query in f_words:
            answer.append(f_words[query])
        elif query[0] == "?" and query[::-1] in b_words:
            answer.append(b_words[query[::-1]])
        else:
            answer.append(0)
            
    return answer
