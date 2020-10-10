class Basket():
    def __init__(self, price, coupons):
        self.price = price
        self.answer = [-1,-1]

        for i, coupon in enumerate(coupons):
            self.apply(i+1, coupon)

    def apply(self, num, coupon):
        price = 0
        flag = 0
        for i in range(4):
            tmp = self.price[i]*(100 - coupon[i])//100
            if tmp < self.price[i]:
                flag = 1
            price += tmp

        if flag == 1 and (self.answer[1] == -1 or self.answer[1] > price):
            self.answer = [num, price]

def solution(price, coupon):
    basket = Basket(price, coupon)
    return basket.answer