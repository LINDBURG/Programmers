def solution(a, b):
    answer = 4
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['MON','TUE','WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer += sum(month[:a-1]) + b-1
    
    return date[answer%7]
