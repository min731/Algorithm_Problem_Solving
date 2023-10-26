import re
import math

def get_words(str_n):

    words = []
    
    check = r'[^a-zA-Z]'
    
    same_cnt = 1
    for i in range(len(str_n)-1):
        
        word = str_n[i]+str_n[i+1]
        
        if re.sub(check,"",word) != word:
            print("word : ",word)
            print("탐지!")
            continue
        
        word = word.upper()
        
        if word in words:
            word += str(same_cnt)
            same_cnt += 1
        
        words.append(word)
    
    return words

def get_Jaccard(words1,words2):
    
    inter = list(set(words1) & set(words2))
    union = list(set(words1) | set(words2))
    
    jaccard = len(inter)/len(union)
    return len(inter)/len(union)

def solution(str1, str2):
    
    words1 = get_words(str1)
    print(words1)
    words2 = get_words(str2)
    print(words2)
    
    if words1==[] and words2==[]:
        return 65536
    
    jaccard = get_Jaccard(words1,words2)
    print(jaccard)
    print(math.floor(jaccard*65536))
    
    return math.floor(jaccard*65536)