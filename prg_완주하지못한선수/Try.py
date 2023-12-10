# from collections import Counter

def solution(participant, completion):
    answer = ''
    
    if not completion:
        return participant.pop()

    participant.sort()
    completion.sort()
    # participant = Counter(participant)
    # completion = Counter(completion)
    
    # print(participant)
    # print(completion)
    
    while participant:
        
        par = participant.pop()
        
        if completion:
            com = completion.pop()
        
        if par != com:
            break
    
    answer = par
    # print(answer)
    
    return answer