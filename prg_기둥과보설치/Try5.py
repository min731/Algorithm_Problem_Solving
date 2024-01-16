def solution(n, build_frame):
    answer = []
    
    ### 설치
    
    # 기둥
    # 1) 바닥 위
    # 2) 보의 한쪽 끝
    # 3) 기둥 위
    
    # 보
    # 1) 한쪽 끝이 기둥 위
    # 2) 양쪽 끝이 다른 보
    
    ### 삭제
    
    # 기둥&보
    # 삭제 후에도 설치 규칙을 만족
    
    wall = [[-1 for j in range(n+1)] for i in range(n+1)]
    
    for frame in build_frame:
        x,y,beam,install = frame
        
        now = wall[x][y]
        if install: 
            if not beam: # 기둥 설치
                if (y==0 and now==-1) or (now==1 or wall[x-1][y]==1)\
                or (wall[x][y-1]==0):
                    wall[x][y]=0
                    print(x,y,"기둥 설치")
            else: # 보 설치
                if (wall[x][y-1]==0)or(wall[x+1][y-1]==0)or\
                (wall[x-1][y]==1 and wall[x+1][y]==1):
                    wall[x][y]=1
                    print(x,y,"보 설치")
        else:
            if not beam: # 기둥 삭제
                if wall[x][y+1]==-1:
                    print(x,y,"기둥 삭제")
                    wall[x][y] = -1
                elif wall[x][y+1]==1:
                    if wall[x-1][y+1]==1 and wall[x+1][y+1]==1:
                        wall[x][y] = -1
                    print(x,y,"기둥 삭제")
            else: # 보 삭제
                if not (wall[x][y-1]==-1 and wall[x-1][y]==1 and wall[x+1][y]==1):
                    wall[x][y] = -1
                    print(x,y,"보 삭제")
    
    for i in range(n+1):
        for j in range(n+1):
            if wall[i][j] != -1:
                answer.append([i,j,wall[i][j]])
    
    answer.sort()
    
    return answer