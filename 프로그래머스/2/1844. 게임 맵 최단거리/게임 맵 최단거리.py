from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*(m) for _ in range(n)]
    
    UD = [-1,1,0,0]
    LR = [0,0,-1,1]
    
    def bfs(x,y):
        
        x, y = x-1, y-1
        queue = deque([(x,y)])
        visited[x][y] = 1

        
        while queue:
            cur_x, cur_y = queue.popleft()
            

            if cur_x == n-1 and cur_y == m-1:
                return visited[cur_x][cur_y]

            # if not queue and (cur_x != n-2 and cur_y == m-1):
            #     return -1
        
            for dx, dy in zip(UD,LR):
                nx = cur_x + dx
                ny = cur_y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and (visited[nx][ny] == 0 or visited[nx][ny] > visited[cur_x][cur_y] + 1):
                        visited[nx][ny] += visited[cur_x][cur_y]+1
                        queue.append((nx,ny))
        return -1

    answer = bfs(1,1)
    return answer