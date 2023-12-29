def solution(dirs):
    answer = 0

    board = {}
    
    for i in range(11):
        for j in range(11):
            for com in ['R','D','L','U']:
                key = str(i)+str(j)+com
                board[key] = 0
    
    move = {'R':[0,1], 'D':[1,0], 'L':[0,-1], 'U':[-1,0]}
    reverse_key = {'R':'L','D':'U','L':'R','U':'D'}
    x,y = 5,5
    
    for dir_ in dirs:
        
        x_, y_ = move[dir_]
        x_next = x+x_
        y_next = y+y_
        
        if x_next>=0 and x_next<=10 and y_next>=0 and y_next<=10:
            
            key1 = str(x)+str(y)+dir_
            x = x_next
            y = y_next
            key2 = str(x)+str(y)+reverse_key[dir_]
            
            if board[key1]==0 :
                board[key1] = 1
                board[key2] = 1         
                answer += 1
    
    return answer