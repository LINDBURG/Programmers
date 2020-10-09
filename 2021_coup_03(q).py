class Audition():
    def __init__(self, k, score):
        self.k = k
        self.score = score
        self.dist = dict()
        self.count = dict()
        self.hacked = set()

        for i in range(1, len(score)):
            self.check(i)

        for key, value in self.count.items():
            if value >= k:
                self.hacked = self.hacked | self.dist[key]

        self.answer = len(score) - len(self.hacked)

    def check(self, i):
        dist = self.score[i-1] - self.score[i]
        if dist not in self.dist:
            self.dist[dist] = set()
            self.count[dist] = 0
        self.dist[dist].update([i-1, i])
        self.count[dist] += 1


def solution(k, score):
    audition = Audition(k, score)
    return audition.answer