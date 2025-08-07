from collections import deque

def is_valid(row, col, max_rows, max_cols):

    # True or False
    return 0 <= row < max_rows and 0 <= col < max_cols

def solution(maps):
    rows, cols = len(maps), len(maps[-1])
    
    # 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS
    queue = deque([(0, 0)])
    
    while queue:
        now_row, now_col = queue.popleft()
        
        # 도착
        if now_row == rows-1 and now_col == cols-1:
            return maps[now_row][now_col]
        
        for dr, dc in directions:
            next_row = now_row + dr
            next_col = now_col + dc
            
            if is_valid(next_row, next_col, rows, cols):
                # 방문 X
                if maps[next_row][next_col] == 1:
                    maps[next_row][next_col] = maps[now_row][now_col] + 1
                    queue.append((next_row, next_col))

    return -1