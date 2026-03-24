"""
1. 원래 개수 = 원래개수 * 2
2. 원래 개수 = 원래개수 - 1

* 덮어쓰기...
0이 될때 걍 넘겨야해
삭제되니까 백트래킹 안되고 bfs로 풀어야함.
"""

from collections import deque

S = int(input()) # 목표
MAX = 1001
visited = [[-1]*MAX for _ in range(MAX)]

def bfs(v,clipboard,sec):
    queue = deque([(v,clipboard,sec)])
    visited[v][clipboard] = 0 # [현재 화면][클립보드]
    
    while queue:
        cur_cnt, cur_clip, cur_sec = queue.popleft()
        
        if cur_cnt == S:
            return visited[cur_cnt][cur_clip]
        
        # 하나 삭제하기
        next_cnt = cur_cnt - 1
        if 0 <= next_cnt < MAX and (visited[next_cnt][cur_clip] == -1 or visited[next_cnt][cur_clip] > cur_sec + 1):
            visited[next_cnt][cur_clip] = cur_sec + 1
            queue.append((next_cnt, cur_clip ,cur_sec+1))
        
        # 복사 하기
        next_clip = cur_cnt
        if 0 < next_clip < MAX and (visited[cur_cnt][next_clip] == -1 or visited[cur_cnt][next_clip] > cur_sec + 1):
            visited[cur_cnt][next_clip] = cur_sec + 1
            queue.append((cur_cnt, next_clip, cur_sec + 1))
        
        # 클립보드에 있는거 화면에 붙여넣기
        next_cnt = cur_cnt + cur_clip
        if cur_clip != 0 and 0 < next_cnt < MAX and (visited[next_cnt][cur_clip] == -1 or visited[next_cnt][cur_clip] > cur_sec + 1):
            visited[next_cnt][cur_clip] = cur_sec + 1
            queue.append((next_cnt, cur_clip, cur_sec + 1))
                
print(bfs(1,0,0))