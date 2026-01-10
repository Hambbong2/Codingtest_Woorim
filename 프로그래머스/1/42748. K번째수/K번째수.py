def solution(array, commands):
    answer = []
    
    for c in commands:
        start = c[0] - 1
        end = c[1]
        temp = array[start:end]
        # 정렬
        temp.sort()
        answer.append(temp[c[2]-1])
        
    return answer