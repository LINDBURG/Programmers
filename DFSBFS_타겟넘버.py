answer = 0

def combine(numbers, target):
    global answer
    if(len(numbers) != 1):
        combine(numbers[1:], target + numbers[0])
        combine(numbers[1:], target - numbers[0])
    elif(target - numbers[0] ==0 or target + numbers[0] ==0):
        answer +=1

def solution(numbers, target):
    global answer
    combine(numbers, target)
    return answer


solution([1, 1, 1, 1, 1], 3)
