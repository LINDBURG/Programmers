def search(left, right, times, n):
    answer = right
    while left <= right:
        mid = (left + right) //2
        cnt = 0
        for time in times:
            cnt += mid // time

        if cnt >= n:
            answer = min(answer, mid)
            right = mid -1
        elif cnt < n:
            left = mid + 1

    return answer

def solution(n, times):
    times.sort()
    mi = 0
    ma = times[-1]* n
    return search(mi, ma, times, n)
