from itertools import combinations

def prime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5) +1):
        if num%i ==0:
            return False
    return True

def solution(nums):
    answer = 0

    comb = list(map(sum,combinations(nums,3)))
    for num in comb:
        if prime(num):
            answer +=1

    return answer
