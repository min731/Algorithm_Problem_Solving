from itertools import combinations

def solution(phone_book):
    
    answer = True
    for p1,p2 in combinations(phone_book,2):
        # print(p1,p2)
        
        len1, len2 = len(p1), len(p2)
        
        if len1>len2 and p1[:len2]==p2 or len1<=len2 and p2[:len1]==p1:
            return False
            
    return answer

print(sorted(["119", "97674223", "1195524421"]	))
