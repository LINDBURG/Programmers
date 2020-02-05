def solution(array, commands):
    answer = []
    
    for data in commands:
        sarr = array[data[0]-1:data[1]]
        sarr.sort()
        answer.append(sarr[data[2]-1])
    return answer
