import math

def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0, 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(progresses) - front)  

    return answer