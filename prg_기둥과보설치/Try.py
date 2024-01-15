def solution(n, build_frame):
    answer = []
    
    wall = [[-1 for j in range(n+1)] for i in range(n+1)] # -1:빈공간,0:기둥,1:보 
    
    for frame in build_frame:
        x, y, beam, install = frame
        
        if install: # 설치
            now = wall[x][y]
            
            if not beam: # 기둥
                # if y-1>=0:
                #     check_d = wall[x][y-1]
                #     if check_d==0:
                #         wall[x][y] = 0
                #         continue
                        
                check_l = wall[x-1][y]
                check_r = wall[x+1][y]
                
                if (y==0 and now==-1) or (check_l==1) or (check_r==1):
                    wall[x][y] = 0
                    print(x,y,"기둥 설치!")

            else: # 보
                check_d = wall[x][y-1]
                check_r_d = wall[x+1][y-1]
                check_l = wall[x-1][y]
                check_r = wall[x+1][y]
                
                if (check_d==0 or check_r_d==0) or (check_l==1 and check_r==1):
                    wall[x][y] = 1
                    print(x,y,"보 설치!")
                    
        else:
            now = wall[x][y]
            if not beam: # 기둥
                check_u = wall[x][y]
                check_u_l = wall[x-1][y+1]
                check_u_r = wall[x+1][y+1]
                
                if not (check_u==1 and check_u_l==1 and check_u_r==1):
                    wall[x][y] = -1
                    print(x,y,"기둥 제거!")
                    
            else: # 보
                check_l = wall[x-1][y]
                check_r = wall[x+1][y]
                
                if not (now==1 and check_l==1 and check_r==1):
                    wall[x][y] = -1
                    print(x,y,"보 제거!")
                    
                    
    # print(wall)
    
    for i in range(n+1):
        for j in range(n+1):
            v = wall[i][j]
            if v != -1:
                answer.append([i,j,v])
        
    answer.sort()
    print(answer)
    return answer

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])