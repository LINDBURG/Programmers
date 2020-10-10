from itertools import permutations

class Number():
    def __init__(self, arr):
        self.arr = arr
        self.answer = 0
        self.perm = permutations(arr, 4)
        #for a,b,c,d in self.perm:
        self.get_max(arr[0], arr[1],arr[2],arr[3])

    def get_max(self, a, b, c, d):
        mx = max(a*b*c*d, a*b*(c+d), a*(b+c)*d, a*(b+c+d), (a+b)*c*d, (a+b)*(c+d), (a+b+c)*d, a+b+c+d)
        if mx > self.answer:
            self.answer = mx

def solution(arr):
    number = Number(arr)
    return number.answer