# 1 0 0 0
# 0 1 1 0
# 1 1 0 0
from collections import deque

UD = [-1,1,0,0]
LR = [0,0,-1,1]

N, M, K = map(int, input().split())

board = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

max_count = 0

flag = False
def bfs(x,y):
    cur_count = 1
    queue = deque([(x,y)])
    visited[x][y] = True

    
    while queue:
        cur_q = queue.popleft()
        dx, dy = cur_q
        
        for i in range(4):
            nx = dx + UD[i]
            ny = dy + LR[i]
            
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    cur_count += 1
                    
    return cur_count

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1: #  이 조건문이 중요!
            max_count = max(max_count, bfs(i,j))
        
print(max_count)