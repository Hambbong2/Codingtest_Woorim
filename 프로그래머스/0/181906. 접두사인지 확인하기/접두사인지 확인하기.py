def solution(my_string, is_prefix):
    answer = 0
    
    if len(is_prefix) > len(my_string):
        return answer
    
    for idx in range(len(is_prefix)):    
        
        if is_prefix[idx] != my_string[idx]:
            answer = 0
            break
        else: 
            answer = 1
     
    
    return answer