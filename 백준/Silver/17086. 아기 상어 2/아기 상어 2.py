from collections import deque

# 상하좌우 대각선 시계방향 # 
move_x = [-1,1,0,0,-1,-1,1,1]
move_y = [0,0,-1,1,-1,1,1,-1]

N, M = map(int, input().split())
graph = []
visited = [[-1]*M for _ in range(N)] # 거리를 큐에 넣거나 방문 리스트에 넣거나
queue = deque()

for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

#1. 모든 상어 위치를 먼저 큐에 삽입 (동시 출발 준비)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 0

while queue:
    cur_x, cur_y = queue.popleft()
    
    
    for dx, dy in zip(move_x, move_y):
        nx = cur_x + dx
        ny = cur_y + dy
        
        if 0<= nx < N and 0<= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                queue.append((nx, ny))
            

# BFS는 가장 먼저 도착한 것이 최단거리이다.
# '최단 거리'에 꽂히면 안되는게, visited에 입력된건 다른 아기상어가 해당 자리로 영역표시 하기 전에 이미 다른 상어가 왔다갈만큼 가까웠다는거다
# 그니까 문제에서 구하는 최댓값은 각 아기상어의 영역표시를 8방향으로 순차적으로 진행할때 교차점 직전의 최댓값이다.

"""
맞아요! 잘 이해했어요. 다시 정리하면:
```
모든 상어가 동시에 출발해서 8방향으로 퍼져나감
→ visited에 저장되는 값 = 가장 가까운 상어까지의 거리
→ 그 중 최댓값 = 가장 외로운 칸 (어떤 상어도 가장 멀리 있는 칸)
"""

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, visited[i][j])
        
print(answer)
    