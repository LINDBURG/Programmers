def solution(n, build_frame):
    answer = []
    dot = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for x,y,a,b in build_frame:
        #print(x,y,a,b)
        if b == 1:#설치
            if a == 0:#기둥
                if y != 0 and dot[x][y] != 1:
                    continue
                dot[x][y+1] = 1
                answer.append([x,y,a])
                #print("기 추")
            else:#보
                if y == 0 or (([x,y-1,0] not in answer and [x+1,y-1,0] not in answer) and (dot[x][y] == 0 or dot[x+1][y] == 0)):
                    continue
                dot[x][y] = 1
                dot[x+1][y] = 1
                answer.append([x,y,a])
                #print("보 추")
        else:#삭제
            if a == 0:#기둥
                if (([x,y+1,1] in answer and [x+1,y,0] not in answer) or ([x-1,y+1,1] in answer and [x-1,y,0] not in answer) or ([x,y+1,0] in answer and [x-1,y+1,1] not in answer and [x,y+1,1] not in answer)):
                    continue
                answer.remove([x,y,a])
                #print("기 삭")
                if [x-1,y+1,1] not in answer and [x,y+1,1] not in answer:
                    dot[x][y+1] = 0
            else:#보
                if ([x-1,y,1] in answer and [x-1,y-1,0] not in answer and [x,y-1,0] not in answer) or ([x+1,y,1] in answer and [x+2,y-1,0] not in answer and [x+1,y-1,0] not in answer) or ([x,y,0] in answer and [x-1,y,1] not in answer and [x,y-1,0] not in answer) or ([x+1,y,0] in answer and [x+1,y,1] not in answer and [x+1,y-1,0] not in answer):
                    continue
                answer.remove([x,y,a])
                #print("보 삭")
                if [x-1,y,1] not in answer and [x,y-1,0] not in answer:
                    dot[x][y] = 0
                if [x+1,y,1] not in answer and [x+1,y-1,0] not in answer:
                    dot[x+1,y] = 0
        #print(dot)
    answer.sort(key=lambda x:(x[0],x[1]))
    return answer
