def solution(dirs):
    answer = 0

    board = [[0 for j in range(11)] for i in range(11)]
    
    # print(board)
    # print(len(board))
    # print(len(board[0]))

    # 우하좌상
    # dx = [0,1,0,-1]
    # dy = [1,0,-1,0]
    
    move = {'R':[0,1], 'D':[1,0], 'L':[0,-1], 'U':[-1,0]}
    x,y = 5,5
    
    for dir_ in dirs:
        
        print("-------------")
        print("이전 x,y", x,y)
        x_, y_ = move[dir_]
        x_next = x+x_
        y_next = y+y_
        print("이후 x,y", x_next, y_next)
        
        if x_next>=0 and x_next<=9 and y_next>=0 and y_next<=9:
            x = x_next
            y = y_next
            if board[x][y]==0:
                board[x][y] = 1
                answer += 1
                print("방문!",answer)
    
    return answer