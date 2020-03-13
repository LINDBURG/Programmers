def solution(n, edge):
    answer = 0
    node = [99999 for i in range(n)]
    node[0] = 1
    link = [[] for i in range(n)]
    for v in edge:
        link[v[0]-1].append(v[1])
        link[v[1]-1].append(v[0])

    queue = [1]
    while queue:
        now = queue.pop(0)
        for l in link[now-1]:
            if node[now-1] + 1 < node[l-1]:
                node[l-1] = node[now-1] + 1
                queue.append(l)

    mx = max(node)
    while mx in node:
        answer += 1
        node.remove(mx)
    return answer
