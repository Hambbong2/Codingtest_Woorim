from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
parent = [0] * MAX

def bfs(v, sec):
    queue = deque([(v, sec)])
    visited[v] = 0 # 방문 배열에 저장하는거는 최단 시간
    parent[v] = v # 나 자신이 부모. 시작점
    
    while queue:
        cur_loc, cur_sec = queue.popleft()
        
        if cur_loc == K:
            path = []
            curr = cur_loc
            
            while curr != N: # 역추적
                path.append(curr)
                curr = parent[curr]
            path.append(N)
            
            return path[::-1], cur_sec
            
        
        for next_loc in [cur_loc+1, cur_loc-1, cur_loc*2]:
            if 0 <= next_loc < MAX and (visited[next_loc] == -1 or visited[next_loc] > cur_sec + 1):
                visited[next_loc] = cur_sec + 1
                parent[next_loc] = cur_loc
                queue.append((next_loc, cur_sec+1))
                
path, sec = bfs(N,0)
print(sec)
print(*path)
