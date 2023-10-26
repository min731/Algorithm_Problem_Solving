from collections import deque

def solution(s):
    
    answer = ''
    
    s = deque(s)
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    word_dict = {word:idx for idx,word in enumerate(words)}
    word = ''
    
    while s:
        
        x = s.popleft()
        
        if x.isdecimal():
            answer += str(x)
        else:
            word += x
        
        if word in word_dict.keys():
            answer += str(word_dict[word]) 
            word = ''
    
    return int(answer)