from collections import deque

UD = [-1,1,0,0]
LR = [0,0,-1,1]

N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    temp = list(input())
    graph.append(temp)
    
start_x, start_y, end_x, end_y = map(int,input().split())
start_x, start_y, end_x, end_y = start_x - 1, start_y - 1, end_x - 1, end_y - 1

        
visited = [[-1]*M for _ in range(N)]

"""
큐에 담을 것: 1초에 갈 수 있는 곳
전제: 먼저 도착하는 곳이 최단거리

주의: 행과 열


현재 코드에서 visited[nx][ny] > visited[cur_x][cur_y] + 1 조건은 논리적으로는 맞지만, 
BFS 특성상 불필요한 연산을 계속 허용하게 됩니다. 이 문제(BOJ 16930 등)의 핵심은
"이미 나보다 빨리 온 놈이 있다면, 그 뒤는 보지도 말고 break" 하는 것입니다.
"""

def bfs(x,y,sec):
    queue = deque([(x,y)])
    visited[x][y] = sec
    
    while queue:
        cur_x, cur_y = queue.popleft()

        if cur_x == end_x and cur_y == end_y:
             return visited[cur_x][cur_y]

        for i in range(4):
            for w in range(1,K+1):
                nx = cur_x + UD[i]*w
                ny = cur_y + LR[i]*w
                
                if 0<= nx < N and 0<= ny < M:
                    
                    if graph[nx][ny] == '#': # '.' 인지 체크가 아니라 갈때마다 '#'인지 체크해서 #만나자마자, 그 방향은 OUT
                        break
                    
                    
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[cur_x][cur_y] + 1
                        queue.append((nx,ny))
                        
                        
                    elif visited[nx][ny] < visited[cur_x][cur_y] + 1: # 방향은 통과했네~ 근데 이미 방문했거나 더 오랜 걸린거면
                        break
                    
                        
    if visited[end_x][end_y] == -1: #큐가 비어서 끝났는데 종착지점이 갱신이 안됐을 때
        return -1
    

print(bfs(start_x, start_y, 0))
        
            
            
            
            