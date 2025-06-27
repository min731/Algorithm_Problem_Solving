from collections import Counter

def solution(participant, completion):

    participant = Counter(participant)
    # print(participant)
    # print(participant.keys())
    # print(participant.values())
    
    for c in completion:
        participant[c] -=1
        
    for key in participant.keys():
        if participant[key] > 0:
            return key
    