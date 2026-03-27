def solution(n, computers):
    """
    유니온 파인드.. 생각안나 
    """
    
    visited = [False] * (n) # 컴퓨터는 0부터 시작
    
    def dfs(n):
    
        visited[n] = True
        
        for idx, v in enumerate(computers[n]):
            if v==1 and not visited[idx]:
                dfs(idx)            
        
        return 1     
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += dfs(i)
    
    return answer