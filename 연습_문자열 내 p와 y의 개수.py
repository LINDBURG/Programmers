from collections import Counter

def solution(s):
    count = Counter(s.lower())
    return count['p'] == count['y']