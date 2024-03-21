def solution(keymap, targets):
    answer = []
    
    for target in targets:
        time = 0
        
        for x in target:
            idx = [101]
            for keys in keymap:
                if x in keys:
                    idx.append(keys.index(x)+1)
            if min(idx)==101:
                time = -1
                break
            else:
                time += min(idx[1:])
        
        answer.append(time)
            
                
    return answer