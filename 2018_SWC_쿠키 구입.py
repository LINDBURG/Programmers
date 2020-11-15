class Basket():
    def __init__(self, cookie):
        self.answer = self.run(cookie)
        
    def run(self, cookie):
        answer = 0
        l_sum = cookie[0]
        r_sum = sum(cookie) - cookie[0]
        for m in range(len(cookie)-1):
            if l_sum < answer or r_sum < answer:
                break
                
            l_idx = 0
            r_idx = len(cookie) - 1
            l_tmp, r_tmp = l_sum, r_sum
            while l_idx <= m and m+1 <= r_idx:
                if l_tmp == r_tmp:
                    if l_tmp > answer:
                        answer = l_tmp
                    break
                elif l_tmp > r_tmp:
                    l_tmp -= cookie[l_idx]
                    l_idx += 1
                else:
                    r_tmp -= cookie[r_idx]
                    r_idx -= 1
                    
            l_sum += cookie[m+1]
            r_sum -= cookie[m+1]
            
        return answer
            

def solution(cookie):
    basket = Basket(cookie)
    return basket.answer