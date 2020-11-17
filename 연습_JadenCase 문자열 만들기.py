def solution(s):
    line = ""
    for idx, c in enumerate(s):
        if idx ==0 or s[idx-1] == " ":
            line += s[idx].upper()
        else:
            line += s[idx].lower()
    return line