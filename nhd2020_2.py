def solution(id_list, k):
    answer = 0
    count = {}
    
    for day in id_list:
        names = day.split()
        names = list(set(names))
        
        for name in names:
            if not name in count:
                count[name] = 1
                answer += 1
            elif count[name] < k:
                count[name] += 1
                answer += 1
    
    return answer
