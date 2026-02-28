# from collections import deque

# def solution(maps):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
    
#     n_row = len(maps) - 1
#     m_col = len(maps[0]) - 1
    
    
#     visited = [[False]*len(maps[0]) for _ in range(len(maps))]
#     start_x, start_y = 0,0
    
#     # bfs 실행
    
#     queue = deque([(start_x, start_y)]) # 아 여기 어떤 형식으로 넣어야 할지.. deque((x,y)) deque([x,y])
#     visited[start_x][start_y] = True
#     min_route = 0
    
#     while queue:
        
#         cur_x, cur_y = queue.popleft()
        
#         for i in range(4): # 4가지 방향에 대해
#             nx, ny = cur_x + dx[i], cur_y + dy[i]
            
#             if 0 <= nx <= n_row and 0 <= ny <= m_col: 
#                 if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    
#                     if nx == n_row and ny == m_col:
#                         return min_route
                    
#                     visited[nx][ny] = True
#                     queue.append((nx,ny))
#                     min_route += 1
                    
        
                
#     return -1


from collections import deque

def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n_row = len(maps) - 1
    m_col = len(maps[0]) - 1
    
    
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    start_x, start_y = 0,0
    
    # bfs 실행
    min_route = 1
    queue = deque([(start_x, start_y, min_route)]) # 아 여기 어떤 형식으로 넣어야 할지.. deque((x,y)) deque([x,y])
    visited[start_x][start_y] = True
    
    while queue:
        
        cur_x, cur_y, min_route = queue.popleft()
        
        if cur_x == n_row and cur_y == m_col:
            return min_route
        
        for i in range(4): # 4가지 방향에 대해
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            if 0 <= nx <= n_row and 0 <= ny <= m_col: 
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    
                    visited[nx][ny] = True
                    queue.append((nx,ny,min_route + 1))
                    
                    
        
                
    return -1


"""
처음 min_route는 방문한 면접을 재고있다. bfs 알고리즘상 최단 거리는 튜플에 저장하여, 그 위치마다 각각의 최단거리를 구해줘야한다.
"""