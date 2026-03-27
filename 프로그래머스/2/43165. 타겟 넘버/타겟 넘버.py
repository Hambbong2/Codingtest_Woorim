def solution(numbers, target):

    
    """
    1
    1+1 , 1-1
    1+1+1,1+1-1, 1-1+1, 1-1-1
    """
    count = [0]
    
    def back_tracking(idx, sum_sub):
        idx += 1
        
        if idx == len(numbers):
            if sum_sub == target:
                count[0] +=1
            
            return
            
        if 0<= idx < len(numbers):
            
            sum_sub += numbers[idx] # 더하기
            back_tracking(idx, sum_sub)
            """
            return하면 idx도 -1 되나?
            """
            sum_sub -= numbers[idx] # 되돌리기
            sum_sub += -numbers[idx] # 빼기
            back_tracking(idx, sum_sub)
    
    back_tracking(-1, 0)
    
    return count[0]