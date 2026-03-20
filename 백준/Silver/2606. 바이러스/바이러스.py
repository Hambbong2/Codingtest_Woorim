from collections import deque

N = int(input())
K = int(input())

linked_list = [[] for _ in range(N+1)]

for _ in range(K):
    idx1, idx2 = map(int, input().split())
    linked_list[idx1].append(idx2)
    linked_list[idx2].append(idx1)

visited = [False] * (N+1)
infection_cnt = 0

def bfs(x):
    global infection_cnt
    queue = deque([x])
    visited[x] = True

    
    while queue:
        cur_x = queue.popleft()
        
        for v in linked_list[cur_x]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                infection_cnt += 1

    return infection_cnt

print(bfs(1))
    
    
    