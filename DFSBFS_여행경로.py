def DFS(order, tickets, airport):
    if len(tickets) ==0:
        return order
    now = airport.index(order[-1])
        
    for  ticket in tickets:
        ntickets = tickets[:]
        norder = order[:]
        if(now == ticket[0]):
            ntickets.remove(ticket)
            norder.append(airport[ticket[1]])
            answer = DFS(norder, ntickets, airport)
            if(answer is not None):
                return answer


def solution(tickets):
    lst = []
    for ticket in tickets:
        lst.extend(ticket)
    lst = list(set(lst))
    lst.sort()

    for i,ticket in enumerate(tickets):
        tickets[i] = [lst.index(ticket[0]), lst.index(ticket[1])]
    tickets.sort()

    answer = DFS(["ICN"], tickets, lst)
    return answer


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
