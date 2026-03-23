"""
여전히 -1 +1 *2 이니까 백트래킹은 못하고 - bfs를 이용해서 가장 먼저 도착한 시간을 구ㅎ자ㅏ
이전 문제 bfs는 각각의 경우의 수를 큐에 더하면서.. 각각 팝하면 조건 확인함.
이때 모든 경우의 수를 구하니까 continue를 한거고.지금은 가장 빠른 시간만 구하면 바로 끝내

"""

from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [-1]*(MAX)


def bfs(v, sec): # 가장 먼저 간 곳이 최단거리를 보장해보자. 원래 bfs는 처음 도달이 최단거리인데 이 문제에서는 원래하던 코드대로 queue에 append만 하면 시간순이 뒤죽박죽이된다. 이를 수정해서 시간 순을 보장해줘야한다.
    queue = deque([(v,sec)])
    visited[v] = 0
    
    while queue:
        cur_loc, cur_sec = queue.popleft()
        
        if cur_loc == K:
            return visited[K]
        
        # 0초를 먼저 검사하고, queue에 넣을때도 0초를 appendleft하고, 1초면 append한다. 시간의 흐름
        next_loc = cur_loc*2
        if 0 <= next_loc < MAX and (visited[next_loc] == -1 or visited[next_loc] > cur_sec):
            visited[next_loc] = cur_sec
            queue.appendleft((next_loc, cur_sec))
        
        for next_loc in [cur_loc+1, cur_loc-1]:
            if 0 <= next_loc < MAX and visited[next_loc] == -1:
                visited[next_loc] = cur_sec + 1
                queue.append((next_loc, cur_sec+1))
                
                    
print(bfs(N,0))
                    
