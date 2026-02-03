def solution(triangle):
    
    """
    DP에서 2가지 방법이 있는데
    - 바텀업
    - 톱다운
    
    여기서는 바텀업이 빠르다.
    맨 아래 두 번째 줄에서 시작해서 아래서부터 가장 큰값을 더해가며 저장해간다 
    """
    # sum_triangle = tirangle # 복사 아니고 객체 참조 -> 안돼
    
    # DP
    for h in range(len(triangle)-2,-1,-1): # range(len(triangle)-2,0,-1) 이 아니다! 마지막 stop에서 0은 포함 안되니까!
        for w in range(len(triangle[h])):
            dmax = max(triangle[h+1][w], triangle[h+1][w+1])
            
            triangle[h][w] += dmax
          

    return triangle[0][0]