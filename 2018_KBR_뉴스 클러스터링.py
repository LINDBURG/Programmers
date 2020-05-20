def solution(str1, str2):
    answer = 1
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = {}
    dict2 = {}
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            if str1[i:i+2] not in dict1:
                dict1[str1[i:i+2]] = 0
            dict1[str1[i:i+2]] += 1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            if str2[i:i+2] not in dict2:
                dict2[str2[i:i+2]] = 0
            dict2[str2[i:i+2]] += 1
            
    s = sum(dict2.values()) + sum(dict1.values())
    inter = 0
    keys = set(list(dict1.keys())+list(dict2.keys()))
    for k in keys:
        if k in dict1 and k in dict2:
            inter += min(dict1[k], dict2[k])
    if s != 0:
        s -= inter
        answer = inter/s
    
    return int(answer*65536)
