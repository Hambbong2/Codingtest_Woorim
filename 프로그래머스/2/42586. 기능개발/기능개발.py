from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for idx in range(len(progresses)):
        rest_q = 100 - progresses[idx]
        
        if rest_q % speeds[idx] != 0:
            rest_day = rest_q // speeds[idx] + 1
        else:
            rest_day = rest_q // speeds[idx]
        
        queue.append(rest_day) # deque([start]) 이렇게 안햇는데 ㄱㅊ은가
        
    
    while queue:
        cur = queue.popleft()
        count = 1
        
        while queue and queue[0] <= cur:
            queue.popleft()
            count+=1
        
        answer.append(count)
        
    return answer
