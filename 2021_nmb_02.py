class Garden():
    def __init__(self, flowers):
        self.flowers = flowers
        self.answer = 0
        self.day = [0 for _ in range(366)]
        for start, end in flowers:
            self.bloom(start, end)

        for i in range(366):
            if self.day[i] > 0:
                self.answer += 1

    def bloom(self, start, end):
        for i in range(start, end):
            self.day[i] += 1

def solution(flowers):
    garden = Garden(flowers)
    return garden.answer