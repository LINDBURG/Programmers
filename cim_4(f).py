'''answer = []
nempty = []

def inp(want, nempty):
    global answer, nempty
    
    if nempty[want] == 0:
        answer.append(want)
        nempty[want] = nempty[want+1]
    else:
        
        
'''
def solution(k, room_number):
    #global answer, nempty
    answer = []
    #nempty = [0] * (k+2)
    for want in room_number:
        for i in range(want, k+1):
            if i not in answer:
                answer.append(i)
                break
    return answer
