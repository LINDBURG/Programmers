def BFS(now, target, graph):
    visited = [0]*len(graph)
    queue = [now]
    
    visited[now] = 1
    while(len(queue) >0):
        now = queue.pop()
        for idx in range(len(graph)):
            if (graph[now][idx] ==1 and idx == target):
                return visited[now]
            elif (graph[now][idx] ==1 and visited[idx] ==0):
                queue.append(idx)
                visited[idx] = visited[now] + 1

    return 0
        



def solution(begin, target, words):
    answer = 0
    graph = []
    
    if target not in words:
        return 0
    words.insert(0, begin)
    for i in range(len(words)):
        tmp = []
        for j in range(i):
            tmp.append(graph[j][i])
        for j in range(i, len(words)):
            cnt = 0
            for k in range(len(begin)):
                if(words[i][k] != words[j][k]):
                    cnt += 1
            if(cnt ==1):
                tmp.append(1)
            else:
                tmp.append(0)
        graph.append(tmp)
    #print(words, graph)

    answer = BFS(0, words.index(target), graph)
    print(answer)
    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
