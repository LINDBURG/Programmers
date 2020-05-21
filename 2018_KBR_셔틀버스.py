def solution(n, t, m, timetable):
    base = 540
    answer = base + t * (n-1)
    conv = []
    
    for time in timetable:
        hh,mm = map(int,time.split(":"))
        conv.append(hh*60+mm)
    conv.sort()
    
    idx = 0
    cnt_n = 0
    while cnt_n < n and idx < len(conv):
        shuttle = []
        while len(shuttle) < m and idx < len(conv) and conv[idx] <= base + cnt_n*t:
            shuttle.append(conv[idx])
            idx += 1
        cnt_n += 1
    
    if len(shuttle) == m:
        answer = shuttle[-1]-1
    
    hh = str(answer // 60)
    if answer // 60 < 10:
        hh = "0" + hh
    mm = str(answer % 60)
    if answer % 60 < 10:
        mm = "0" + mm
        
    return hh + ":" + mm
