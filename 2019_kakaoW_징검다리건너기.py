def binary(left,right, stones, k):

    while left <=right:
        flag = 1
        cnt = 0
        mid = (left+right)//2

        for num in stones:
            if num < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                flag = 0
                break

        if flag == 0:
            right = mid-1
        else:
            left = mid + 1
    if flag ==0:
        return mid-1
    else:
        return mid


def solution(stones, k):
    answer = binary(0,max(stones), stones, k)
    return answer
