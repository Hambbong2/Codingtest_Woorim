"""
노가다 완탐
"""

UD = [1,0]
LR = [0,1]

N = int(input())
graph = []

for _ in range(N):
    temp = input() # list("CCP")를 하면 ["CCP"]가 되는 게 아니라 ['C', 'C', 'P']가 됩니다.
    graph.append(list(temp))
   
def get_max_count():
    
    max_cnt = 0
    for i in range(N):
        cnt = 1
        # 가로 검사
        for j in range(1,N):
            if graph[i][j] == graph[i][j-1]:
                cnt +=1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        
        cnt = 1
        # 세로 검사
        for j in range(1,N):
            if graph[j][i] == graph[j-1][i]:
                cnt +=1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt
        
        
            

max_candy = 0
for i in range(N):
    for j in range(N):
        
        if j+1 < N and graph[i][j] != graph[i][j+1]:                
            temp = graph[i][j]
            graph[i][j] = graph[i][j+1]
            graph[i][j+1] = temp
            
            max_candy = max(max_candy, get_max_count())
            
            temp = graph[i][j]
            graph[i][j] = graph[i][j+1]
            graph[i][j+1] = temp
        
        if i+1 < N and graph[i][j] != graph[i+1][j]:
            temp = graph[i][j]
            graph[i][j] = graph[i+1][j]
            graph[i+1][j] = temp
            
            max_candy = max(max_candy, get_max_count())
            
            temp = graph[i][j]
            graph[i][j] = graph[i+1][j]
            graph[i+1][j] = temp

print(max_candy)