def find_square(i,j,board):
    
    b1 = board[i][j]
    b2 = board[i][j+1] 
    b3 = board[i+1][j] 
    b4 = board[i+1][j+1] 
    
    if b1==b2 and b2==b3 and b3==b4:
        return True
    else:
        return False

def fill_board():
    
    return

def solution(m, n, board):
    answer = 0 
    find_block = True
    tmp = ['' for i in range(n)]

    for i in range(m):
        board[i] = list(board[i])
        
    while find_block:
        
        find_block = False
        find_xy = []
        
        for i in range(m-1): # "TTTANT"
            for j in range(n-1): # T,T,T,A,N,T
                if board[i][j]==' ':
                    continue
                elif find_square(i,j,board):

                    find_xy.append([i,j])
                    find_block = True

        for x,y in find_xy:
      
            board[x][y] = ""
            board[x+1][y] = ""
            board[x][y+1] = ""
            board[x+1][y+1] = ""
            
        
        for i in range(m):
            print(board[i])
        
        tmp = ['' for _ in range(n)]
        for i in range(m):
            row = board[i]
            for j in range(n):
                tmp[j] += row[j]

        for i in range(n):
            
            if len(tmp[i])<m:
                tmp[i] = " "*(m-len(tmp[i])) + tmp[i]
        
        new_board = ['' for i in range(m)]
        for i in range(n):
            row = tmp[i] # ' TTTT'
            for j in range(m):
                new_board[j] += row[j]

        for i in range(m):
            new_board[i] = list(new_board[i])
        board = new_board

    for i in range(m):
        for j in range(n):
            if board[i][j]==' ':
                answer += 1
        
    return answer