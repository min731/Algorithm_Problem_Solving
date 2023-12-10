def solution(participant, completion):
    answer = ''
    
    if not completion:
        return participant.pop()

    participant.sort()
    completion.sort()

    while participant:
        
        par = participant.pop()
        
        if completion:
            com = completion.pop()
        
        if par != com:
            break
    
    answer = par

    return answer