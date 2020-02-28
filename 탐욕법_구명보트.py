def solution(people, limit):
    answer = 0
    people.sort()
    
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        w2 = people[j]
        j -= 1
        
        if people[i] + w2 <= limit:
            i += 1
        
    return answer
