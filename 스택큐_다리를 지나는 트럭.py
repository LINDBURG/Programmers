def solution(bridge_length, weight, truck_weights):
    answer = 1
    wsum = 0
    con = []
    while(truck_weights or con):
        if len(truck_weights) >0:
            if wsum + truck_weights[0] <= weight:
                truck = truck_weights[0]
                truck_weights.remove(truck)
                for i in range(len(con), bridge_length-1):
                    con.append(0)
                con.append(truck)
                wsum += truck
        wsum -= con[0]
        con = con[1:]
        answer += 1
    return answer

solution(2, 10, [7, 4, 5, 6])
