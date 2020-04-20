def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    arrs = []
    for string in s:
        arr = string.split(',')
        arr = list(map(int,arr))
        arrs.append(arr)
    arrs.sort(key=len)
    for arr in arrs:
        for num in arr:
            if not num in answer:
                answer.append(num)
                break
                
    return answer
