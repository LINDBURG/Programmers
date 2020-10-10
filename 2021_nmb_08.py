class Elevator():
    def __init__(self, money, cost):
        self.money = money
        self.cost = cost
        self.answer = 0

        start = 0
        end = 0
        n_sum = 0
        while end < len(self.cost):
            while end < len(self.cost) and n_sum <= money:
                n_sum += self.cost[end]
                end += 1
            if end - start -1 > self.answer:
                self.answer = end - start -1
            while n_sum > money:
                n_sum -= self.cost[start]
                start += 1

def solution(money, cost):
    elevator = Elevator(money, cost)
    return elevator.answer