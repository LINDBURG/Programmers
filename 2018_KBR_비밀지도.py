def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        #print(num1, num2)
        line = ""
        for i in range(n):
            if num1%2 == 1 or num2 % 2 == 1:
                line = "#" + line
            else:
                line = " " + line
            num1 = num1 // 2
            num2 = num2 // 2
        answer.append(line)
    return answer