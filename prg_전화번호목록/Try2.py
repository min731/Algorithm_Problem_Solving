def solution(phone_book):

    phone_book = sorted(phone_book,key=len)

    for num in phone_book:
        tmp = phone_book
        tmp.remove(num)
        
        for x in tmp:
            if num==x[:len(num)]:
                return False
            
    return True