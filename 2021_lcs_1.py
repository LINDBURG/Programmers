from itertools import combinations

def solution(weight):
    answer = [0,0]
    weight.sort(reverse = True)

    for l_num in range(len(weight)-1,0,-1):
        for left in combinations(weight, l_num):
            l_sum = sum(left)
            right_pool = weight[:]
            for l in left:
                right_pool.remove(l)

            for r_num in range(len(weight) - l_num, 0, -1):
                for right in combinations(right_pool, r_num):
                    if l_sum == sum(right) and l_sum > answer[1]:
                        answer = [l_num + r_num, l_sum]

    return answer