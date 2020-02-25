import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    rsup = [-x for x in supplies]
    heap = [(rs, date, sup) for rs, date,sup in zip(rsup, dates, supplies)]
    heapq.heapify(heap)
    
    while stock < k:
        tmp = []
        while True:
            dns = heapq.heappop(heap)
            if dns[1] <= stock:
                stock += dns[2]
                answer += 1
                break
            else:
                tmp.append(dns)
                
        
        for dns in tmp:
            heapq.heappush(heap, dns)
    print(answer)
    return answer

solution(4, [4,10,15], [20,5,10], 30)
