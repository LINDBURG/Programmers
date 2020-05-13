def solution(record):
    message = []
    answer = []
    nick = {}
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            message.append([1,r[1]])
            nick[r[1]] = r[2]
        elif r[0] == "Leave":
            message.append([0,r[1]])
        else:
            nick[r[1]] = r[2]
        
            
    for stat,uid in message:
        if stat == 1:
            answer.append(nick[uid] + "님이 들어왔습니다.")
        else:
            answer.append(nick[uid] + "님이 나갔습니다.")
    #print(nick)
    return answer
