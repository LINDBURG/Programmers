def solution(key, lock):
    fill = []
    blank = 0
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                fill.append([i,j])

    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                blank += 1
    if blank == 0:
        return True
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                continue
            for base in fill:
                cnt = 0
                flag = 0
                for now in fill:
                    x = now[0] - base[0]
                    y = now[1] - base[1]
                    x, y = i + x, j + y
                    if x < 0 or x >= len(lock) or y < 0 or y >= len(lock):
                        continue
                    elif lock[x][y] == 0:
                        cnt += 1
                    else:
                        flag = 1
                        break
                if flag == 0 and cnt == blank:
                    return True

                cnt = 0
                flag = 0
                for now in fill:
                    x = now[0] - base[0]
                    y = now[1] - base[1]
                    x, y = i + y, j - x
                    if x < 0 or x >= len(lock) or y < 0 or y >= len(lock):
                        continue
                    elif lock[x][y] == 0:
                        cnt += 1
                    else:
                        flag = 1
                        break
                if flag == 0 and cnt == blank:
                    return True

                cnt = 0
                flag = 0
                for now in fill:
                    x = now[0] - base[0]
                    y = now[1] - base[1]
                    x, y = i - x, j - y
                    if x < 0 or x >= len(lock) or y < 0 or y >= len(lock):
                        continue
                    elif lock[x][y] == 0:
                        cnt += 1
                    else:
                        flag = 1
                        break
                if flag == 0 and cnt == blank:
                    return True

                cnt = 0
                flag = 0
                for now in fill:
                    x = now[0] - base[0]
                    y = now[1] - base[1]
                    x, y = i - y, j + x
                    if x < 0 or x >= len(lock) or y < 0 or y >= len(lock):
                        continue
                    elif lock[x][y] == 0:
                        cnt += 1
                    else:
                        flag = 1
                        break
                if flag == 0 and cnt == blank:
                    return True


    return False
