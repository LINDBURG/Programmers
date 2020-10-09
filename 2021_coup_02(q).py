import heapq as hq

class Kiosk():
    def __init__(self, n, customers):
        self.n = n
        self.count = [0 for _ in range(n)]
        self.heap = [[0,i] for i in range(n)]
        hq.heapify(self.heap)
        self.month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        self.customers = map(self.convert, customers)

        for time, cost in self.customers:
            self.enqueue(time, cost)

        self.answer = max(self.count)


    def enqueue(self, start_time, cost):
        end_time, nid = hq.heappop(self.heap)
        if end_time > start_time:
            nxt_time = end_time + cost
        else:
            nxt_time = start_time + cost

        hq.heappush(self.heap, [nxt_time, nid])
        self.count[nid] += 1


    def convert(self, line):
        MM, DD, HH, mm, SS, cost = int(line[:2]), int(line[3:5]), int(line[6:8]), int(line[9:11]), int(line[12:14]), int(line[15:])
        time = SS + 60*(mm + 60*(HH + 24*(self.month[MM-1] + DD -1)))

        return [time, cost *60]



def solution(n, customers):
    kiosk = Kiosk(n, customers)
    return kiosk.answer