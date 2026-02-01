def solution(rows, columns, queries):
    original_map = [[(i*columns+j+1) for j in range(columns)] for i in range(rows)]
    answer = []
    
    for q in queries:
        min_value = rotation_loop(q, original_map)
        answer.append(min_value)
    
    
    return answer

def rotation_loop(query, matrix): 
    
    x1 = query[0] - 1 # 미리 0번부터 좌표 맞추기
    y1 = query[1] - 1
    x2 = query[2] - 1
    y2 = query[3] - 1
    
    
    min_value = matrix[x1][y1]
    temp = matrix[x1][y1]
    
    # 반드시 아래 순서를 지켜야 한다. 핵심은 대체해도 상관없는 '빈 곳'을 '채우는' 것이라서
    # 1. 왼쪽 변(위로 이동)
    for i in range(x1,x2): 
        matrix[i][y1] = matrix[i+1][y1]
        min_value = min(min_value, matrix[i][y1])
    
    # 2. 아래쪽 변(왼쪽으로 이동)
    for i in range(y1,y2):
        matrix[x2][i] = matrix[x2][i+1]
        min_value = min(min_value, matrix[x2][i])
    
    # 3. 오른쪽 변(아래로 이동)
    for i in range(x2,x1,-1): # 대체되는게 start
        matrix[i][y2] = matrix[i-1][y2] # 여기조심해 range에서 -1하는건 i가 루프를 돌며 -1 한다는거고 여기는 그 루프마다 대체하게 하는 것들이니까! -1이야.
        min_value = min(min_value, matrix[i][y2])
        
    # 4. 위쪽 변(오른쪽으로 이동)
    for i in range(y2,y1,-1):
        matrix[x1][i] = matrix[x1][i-1]
        min_value = min(min_value, matrix[x1][i])
    
    matrix[x1][y1+1] = temp # 반드시 나머지!!
    
    return min_value
    