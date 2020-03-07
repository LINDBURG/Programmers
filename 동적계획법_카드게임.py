def solution(left, right):
    answer = 0
    xy = [[-1 for i in range(len(left) +1)] for j in range(len(right) +1)]
    xy[0][0] = 0
    mx = -1
    for i in range(len(left)):
        for j in range(len(right)):
            if xy[i][j] != -1:
                if left[i] > right[j]:
                    xy[i][j+1] = max(xy[i][j] + right[j], xy[i][j+1])
                else:
                    xy[i+1][j+1] = max(xy[i][j], xy[i+1][j+1])
                    xy[i+1][j] = max(xy[i][j], xy[i+1][j])
                mx = max(mx, xy[i][j+1], xy[i+1][j+1], xy[i+1][j])

    return mx
