def solution(sizes):

    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        
        # 편의상, 가로: 큰쪽/ 세로: 작은쪽이라 함.
        width = max(w,h)
        height = min(w,h)
        
        # 가로는 명함의 모든 큰쪽을 커버해야 하고
        # 세로는 명함의 모든 작은쪽을 커버해야 함
        max_w = max(max_w, width)
        max_h = max(max_h, height)
        
    
    return max_w * max_h


