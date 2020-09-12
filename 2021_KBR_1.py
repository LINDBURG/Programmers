from itertools import combinations

class Order():
    def __init__(self,orders, course):
        self.orders = [sorted(list(order)) for order in orders]
        self.course = course
        self.course_max = [0 for _ in range(11)]
        self.course_dict = [dict() for _ in range(11)]
        self.result = []
        
        for num in course:
            self.make_course(num)
        self.check()
        
    def make_course(self, num):
        course_dict = self.course_dict[num]
        for order in self.orders:
            if len(order) >= num:
                for tmp_dict in map(''.join, combinations(order,num)):
                    if tmp_dict in course_dict:
                        course_dict[tmp_dict] += 1
                    else:
                        course_dict[tmp_dict] = 1
                    if self.course_max[num] < course_dict[tmp_dict]:
                        self.course_max[num] = course_dict[tmp_dict]
                        
    def check(self):
        tmp_result = []
        for num in self.course:
            course_dict = self.course_dict[num]
            course_max = self.course_max[num]
            if course_max < 2:
                continue
            for key,value in course_dict.items():
                if value == course_max:
                    tmp_result.append(key)
        self.result += sorted(tmp_result)
            

def solution(orders, course):
    order = Order(orders,course)
    return order.result