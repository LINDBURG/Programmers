def solution(msg):
    answer = []
    dic = {chr(i):i-64 for i in range(65,91)}
    
    start = 0
    while start < len(msg):
        for end in range(len(msg),start,-1):
            if msg[start:end] in dic:
                break
        w = msg[start:end]
        answer.append(dic[w])
        if end < len(msg):
            c = msg[end]
            dic[w+c] = len(dic) + 1
        start = end
    #print(dic)
    return answer