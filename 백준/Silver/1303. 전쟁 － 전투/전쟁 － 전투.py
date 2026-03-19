"""
(0,0) (0,1)
(1,0) (1,1)

"""
from collections import deque

UD = [-1,1,0,0]
LR = [0,0,-1,1]

N, M = map(int, input().split())
map = []

for _ in range(M):
    str_line = input()
    map.append(str_line)

visited = [[False]* N for _ in range(M)]

def bfs(x,y,color):
    # global team_cnt
    queue = deque([(x,y)])
    visited[x][y] = True 
    team_cnt = 1
      
    while queue:
        cur_cord = queue.popleft()
        dx = cur_cord[0]
        dy = cur_cord[1]
        for idx in range(4): # 상 하 좌 우 
            nx = dx + UD[idx]
            ny = dy + LR[idx]
            
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and map[nx][ny] == color:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    team_cnt += 1

    return team_cnt

B_power = 0
W_power = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            team_cnt = 0
            result = bfs(i,j,map[i][j])

            if map[i][j] == 'B':
                B_power += result**2
            else:
                W_power += result**2
 
print(W_power, B_power)

                       