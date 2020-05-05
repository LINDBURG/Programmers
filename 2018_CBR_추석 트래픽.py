def solution(lines):
    answer = 1
    conv = []
    start = 0
    end = 0
    
    for line in lines:
        hh = int(line[11:13])*3600000
        mm = int(line[14:16])*60000
        ss = int(float(line[17:23])*1000)
        elapse = int(float(line[24:-1])*1000)
        conv.append([hh+mm+ss, hh+mm+ss - elapse + 1])
    conv.sort()
    
    while start<len(conv):
        cnt = 0
        for i in range(end,len(conv)):
            if conv[i][0] < conv[start][0] + 1000:
                end = i
            elif conv[i][1] < conv[start][0] + 1000:
                cnt += 1
                
        if end - start + 1 + cnt > answer:
            answer = end - start + 1 + cnt
        start += 1
    return answer
