import copy

def solution(arr):
    answer = []
    
    tmp = arr.copy()
    tmp.sort(reverse=True)
    arr.remove(tmp[-1])

    
    if arr:
        answer = arr
    else:
        answer = [-1]
    
    return answer