def solution(numbers):
    answer = 0
    prime = []
    
    cnt = [0] * 10
    for n in numbers:
        cnt[int(n)] += 1
        
    
    for length in range(1,len(numbers)+1):
        tmp =""
        flag = 0
        
        word(length, tmp, cnt, prime, flag)

    for i in prime:
        if(isprime(i)):
            answer +=1
    
    return answer


def word(length, wd, arr, prime, flag):
    start = 0
    if flag == 0:
        start = 1
    
    if(length<=len(wd)):
        prime.append(int(wd))
    else:
        for i in range(start, 10):
            if(arr[i] != 0):
                narr = arr[:]
                nwd = wd

                narr[i] -= 1
                nwd += str(i)
                
                if (i != 0):
                    flag = 1

                word(length, nwd, narr, prime, flag)

def isprime(n):
    if (n ==1):
        return False

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n%i == 0:
            return False

    return True

#print(solution("17"))
