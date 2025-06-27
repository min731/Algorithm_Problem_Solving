def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # print(hash_map)
    for phone_number in phone_book:
        temp = ""
        print("phone_number : ", phone_number)
        for number in phone_number:
            print("number : ", number)
            temp += number
            if temp in hash_map and temp != phone_number:
                # print(hash_map)
                print("temp : ", temp)
                answer = False
    return answer

# print(solution(["119", "5521194421"]))
# print(solution(["119", "1195521194421"]))
# print(solution(["123","456","789"]))
