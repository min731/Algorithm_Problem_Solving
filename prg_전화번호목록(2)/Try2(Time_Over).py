from collections import Counter
def solution(phone_book):
    
    phone_book = Counter(phone_book)
    # print(phone_book)
    for p1 in phone_book:
        for p2 in phone_book:
            
            if p1!=p2:
                len1, len2 = len(p1), len(p2)
                if len1 > len2 and p1[:len2] == p2 or len1 <= len2 and p2[:len1] == p1:
                    return False

    return True


print(True if "star" in "loststar2" else False)