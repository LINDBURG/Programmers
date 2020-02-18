
def dsort(depth, arr):
    out = []
    left = []
    mid = []
    right = []
    for i in range(10):
        left.append([])
        mid.append([])
        right.append([])

    for num in arr:
        tmp = ""
        for i in range(len(num)):
            tmp += num[i%depth]
        if(len(num) == depth):
            mid[int(num[depth-1])].append(num)
        elif(tmp < num):
            right[int(num[depth-1])].append(num)
        elif(num[0] == num[depth] and num[1:depth] < num[:depth-1]):
            right[int(num[depth-1])].append(num)            
        else:
            left[int(num[depth-1])].append(num)

    for i in range(10):
        if(len(left[i]) != 0):
            out.extend(dsort(depth+1, left[i]))
        if(len(mid[i]) != 0):
            out.extend(mid[i])
        if(len(right[i]) != 0):
            out.extend(dsort(depth+1, right[i]))

    return out
        

def solution(numbers):
    numbers.sort()
    for i,n in enumerate(numbers):
        numbers[i] = str(n)

    out = dsort(1, numbers)
    answer = ""
    flag = 0
    print(out)
    for num in range(len(out)-1,-1, -1):
        if(out[num]!="0"):
            flag = 1
        if(flag ==1 or num==0):
            answer += out[num]
    print(answer)
    return answer



solution([12,121])
