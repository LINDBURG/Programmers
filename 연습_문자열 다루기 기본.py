def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
    for c in s:
        if c.isalpha():
            answer = False
            break
    return answer