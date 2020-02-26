def solution(name):
    answer = 0
    name = list(name)

    now = 0
    while list(filter(lambda x: x !='A', name)):
        c = ord(name[now])
        mn = min(c - ord('A'), ord('Z') - c + 1)
        answer += mn
        name[now] = 'A'
        
        for i in range(1, (len(name)+ 2) // 2):
            if name[(now + i) % len(name)] =='A' and name[now - i] == 'A':
                continue
            elif name[(now + i) % len(name)] != 'A':
                now = (now + i) % len(name)
                answer += i
                break
            elif name[now - i] != 'A':
                now = (now + len(name) -i) % len(name)
                answer += i
                break
        
        
    print(answer)
    return answer

solution("AABAAAA")
