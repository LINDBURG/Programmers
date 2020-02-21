def solution(heights):
    answer = []
    heights.reverse()
    for i in range(len(heights)):
        height = len(heights)
        
        for j in range(i+1, len(heights)):
            if heights[i] < heights[j]:
                height = j
                break
        answer.append(len(heights)-height)
    answer.reverse()
    return answer


solution([6,9,5,7,4])
