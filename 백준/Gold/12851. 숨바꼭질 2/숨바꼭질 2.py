from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [-1] * MAX # checkpoint: 1. 0이 아니라 -1인 이유, 2. visited는 방문 횟수가 아니다 3. [-1]*(K+1) 안되는 이유

"""
1. 숫자의 흐름이 한방향이 아님. -1과 +1 공존
2. 최단시간를 물음.(백트래킹은 한놈만 파고 안될때 그제서야 한발짜 물러서)
3. 최단시간뿐만 아니라 방법의 가짓수도 물음
"""
min_sec = float('inf')
count = 0
    
def bfs(): 
    global min_sec, count
    queue = deque([(N, 0)]) # 현재 위치, 누적 시간
    visited[N] = 0    
    
    while queue:
        cur_location, sec = queue.popleft()

        # [최적화] 이미 최단 시간을 찾았는데, 더 늦게 도착한 놈들은 무시
        if min_sec != float('inf') and sec > min_sec:
            break
        
        # 종료 조건
        if cur_location == K: # 몇번 경로를 거치든 도착지까지 왔어. 근데 거쳐간 놈이 잇늕 없는지 확인
            if min_sec == float('inf'): # 만약 이게 내가 처음 찾은 거라면 이게 최단 시간
                min_sec = sec
                count = 1
            elif sec == min_sec: # 
                count += 1
            continue
            

        # 목표까지 왔던 곳도 돌아가고 순간이동하며 거쳐감. 그 와중에 처음간 곳이나 이미 누가 갔지만 나랑 시간이 똑같을 때 방문 횟수를 카운트
        for next_location in [cur_location*2, cur_location+1, cur_location-1]:
            
            if 0<=next_location< MAX:
                if visited[next_location] == -1 or visited[next_location] == sec+1: # 1. 처음가보거나 2. 동일한 시간으로 같은 위치에 도착할 떄 <- 아니 시간이 아니라 방문횟수 넣어야하는거아냐?
                    queue.append((next_location, sec+1))
                    visited[next_location] = sec + 1

bfs()                
print(min_sec)
print(count)