def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        info = info.split(',')
        time = (int(info[1][0:2]) - int(info[0][0:2]))*60 + (int(info[1][3:5]) - int(info[0][3:5]))
        m_name = info[2]
        m_len = len(info[3]) - info[3].count("#")
        music = info[3]*(time//m_len)
        t_left = time%m_len
        idx = 0
        while t_left >0:
            t_left -= 1
            music += info[3][idx]
            idx += 1
            if idx < len(info[3]) and info[3][idx] == '#':
                idx += 1
                music += '#'
        
        if m[-1] == '#' and m in music:
            answer.append((-time,m_name))
        elif m[-1] != '#' and music.count(m) > music.count(m+'#'):
            answer.append((-time,m_name))
        
    if len(answer)==0:
        return "(None)"
    else:
        answer.sort()
        return answer[0][1]