def solution(phone_book):
    answer = True
    phone_book.sort(key= lambda x: len(x))

    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if(phone_book[i] == phone_book[j][:l]):
               return False
    return answer

solution(["12", "123", "1235", "567", "88"])
