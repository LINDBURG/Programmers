def mxbud(budgets, M):
    avg = M / len(budgets)
    rev = 0
    new = []

    for bud in budgets:
        if bud <= avg:
            rev += avg - bud
        else:
            new.append(bud)

    if sum(budgets) <= M:
        return max(budgets)
    if min(new) < avg + (rev/len(new)):
        return mxbud(new, avg*len(new) + rev)
    else:
        return avg + (rev/len(new))


def solution(budgets, M):
    answer = mxbud(budgets, M)
    return int(answer)
