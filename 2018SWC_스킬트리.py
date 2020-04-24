def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        cnt = 0
        flag = 1
        for s in tree:
            if s in skill and skill[cnt] ==s:
                cnt += 1
            elif s in skill and skill[cnt] != s:
                flag = 0
                break
        if flag == 1:
            answer += 1
    return answer
