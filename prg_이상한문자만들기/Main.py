def solution(s):
    answer = ''
    lst = []
    s = s.split(" ")
    
    for word in s:
        tmp = ''
        for i,x in enumerate(word):
            if i%2==0:
                tmp += x.upper()
            else:
                tmp += x.lower()
        lst.append(tmp)
    
    # print(" ".join(lst))
    return " ".join(lst)