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
    # print(tmp)
    # return 
    for i in range(m):
        board[i] = list(board[i])
        
    while find_block:
        
        print("-------------------------------")
        find_block = False
        find_xy = []
        
        for i in range(m-1): # "TTTANT"
            for j in range(n-1): # T,T,T,A,N,T
                if board[i][j]==' ':
                    continue
                elif find_square(i,j,board):
                    # answer.add((i,j))
                    # answer.add((i+1,j))
                    # answer.add((i,j+1))
                    # answer.add((i+1,j+1))

                    find_xy.append([i,j])
                    find_block = True
#         dx = [0,1,0,1]
#         dy = [0,0,1,1]
        
        for x,y in find_xy:
            # for i in range(4):
                # if board[x+dx[i]][y+dy[i]]!=" ":
                #     answer += 1
                # board[x+dx[i]][y+dy[i]]=" "
                
                
            board[x][y] = ""
            board[x+1][y] = ""
            board[x][y+1] = ""
            board[x+1][y+1] = ""
            
        
        for i in range(m):
            print(board[i])
        
        tmp = ['' for _ in range(n)]
        for i in range(m):
            row = board[i]
            # print("row : ",row)
            for j in range(n):
                # print("row[j]",row[j])
                tmp[j] += row[j]
            
            # print(" tmp :",tmp)
        #     if len(tmp)<n:
        #         tmp = " "*(n-len(tmp)) + tmp
        # print(" tmp :",tmp)

        
        for i in range(n):
            
            if len(tmp[i])<m:
                tmp[i] = " "*(m-len(tmp[i])) + tmp[i]
            # print(len(tmp[i]))
        # print(" tmp :",tmp)
        # break
        
        new_board = ['' for i in range(m)]
        # print(new_board)
        for i in range(n):
            row = tmp[i] # ' TTTT'
            # print("row : ",row )
            for j in range(m):
                # print(row[j])
                new_board[j] += row[j]
                # break    
        
        # print(new_board)
        
        #     board[m] = list(tmp[i])
        # print(tmp)
        # print(board)
        print("-----------------")
        for i in range(m):
            new_board[i] = list(new_board[i])
            print(new_board[i])
        # print(new_board)
        board = new_board
        # break
        print("answer : ",answer)
        
    for i in range(m):
        for j in range(n):
            if board[i][j]==' ':
                answer += 1
        
    return answer