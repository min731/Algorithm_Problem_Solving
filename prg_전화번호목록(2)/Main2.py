def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(phoneBook)
    print(phoneBook[1:])
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))