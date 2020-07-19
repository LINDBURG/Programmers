def solution(files):
    answer = []
    for file in files:
        head, number = "", ""
        idx = 0
        while idx < len(file):
            if not file[idx].isdigit():
                head += file[idx]
                idx += 1
            else:
                break
        while idx < len(file):
            if file[idx].isdigit():
                number += file[idx]
                idx += 1
            else:
                break
        
        head = head.lower()
        number = int(number)
        answer.append((head, number, file))
    
    tmp = sorted(answer, key=lambda x: (x[0],x[1]))
    answer = [file[2] for file in tmp]
    #print(answer)
    return answer