def solution(words, queries):
    answer = []
    h_words = {}
    for word in words:
        n_word = "?"*len(word)
        if n_word not in h_words:
            h_words[n_word] = 1
        else:
            h_words[n_word] += 1
        
        for i in range(1,len(word)):
            n_word = "?"*i + word[i:]
            if n_word not in h_words:
                h_words[n_word] = 1
            else:
                h_words[n_word] += 1
            
            n_word = word[:len(word)-i] + "?"*i
            if n_word not in h_words:
                h_words[n_word] = 1
            else:
                h_words[n_word] += 1
    
    for query in queries:
        if query in h_words:
            answer.append(h_words[query])
        else:
            answer.append(0)
            
    return answer
