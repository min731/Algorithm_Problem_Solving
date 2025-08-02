def get_alphabet(c):
    return min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

def solution(name):
    answer = sum(get_alphabet(c) for c in name)
    
    n = len(name)
    min_move = n-1
    
    for i in range(n):

        next_idx = i+1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        if next_idx == n:
            min_move = min(min_move, i)
            break
        else:
            move_forward = i*2 + (n - next_idx)
            move_backward = (n - next_idx)*2 + i
            
            min_move = min(min_move, move_forward, move_backward)
    answer += min_move

    return answer