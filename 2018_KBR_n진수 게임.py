def solution(n, t, m, p):
    answer = ''
    over = ['A', 'B', 'C', 'D', 'E', 'F']
    num = -1
    idx = 0
    num_len = 0
    p-= 1
    while len(answer) < t:
        while True:
            idx = (num_len + idx) % m
            num += 1
            if num == 0 or num >= n ** num_len:
                num_len += 1
            if idx <= p and p -idx < num_len:
                dist = p - idx
                break
            if m - idx + p < num_len:
                dist = m - idx + p
                break
        
        tmp_num = num
        tmp_str = ''
        if num == 0:
            tmp_str = '0'
        while tmp_num > 0:
            remainder = tmp_num % n
            if remainder >= 10:
                remainder = over[remainder-10]
            else:
                remainder = str(remainder)
            tmp_str = remainder + tmp_str
            tmp_num = tmp_num // n
            
        #print(num, num_len, idx, m- idx + p -1, dist)
        #print(tmp_str)
        answer += tmp_str[dist]
    #print(answer)
    return answer