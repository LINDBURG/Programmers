class Number():
    def __init__(self, N):
        self.n = N
        self.answer = [0,0]

        for i in range(2, 10):
            self.change(i)

    def change(self, k):
        tmp = 1
        n = self.n
        while n :
            res = n % k
            n //= k
            if res != 0:
                tmp *= res

        if tmp >= self.answer[1]:
            self.answer = [k,tmp]

def solution(N):
    number = Number(N)
    return number.answer