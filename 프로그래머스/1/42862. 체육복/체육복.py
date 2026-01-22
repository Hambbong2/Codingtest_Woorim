def solution(n, lost, reserve):
    count = n - len(lost) # 수업을 들을 수 잇는 학생 수 
    
    # 중복 번호 찾기      
    temp = []
    reserve.sort()
    lost.sort()
    max_arr = reserve
    min_arr = lost
    
    if len(lost) > len(reserve):
        max_arr = lost
        min_arr = reserve
    
    for max_a in max_arr:
        for min_a in min_arr:
            if max_a == min_a:
                temp.append(max_a)
        
        
                
    # 중복 되는 번호 빼기
    count = count + len(temp) # 체육복을 잃어도 여벌이 잇어서 수업을 들을 수 있음
    
    # 여벌을 본인이 사용한 학생 수 는 -99처리
    for t in temp:
        reserve[reserve.index(t)] = -99
        lost[lost.index(t)] = -99
    
    # 빌려줄 수 잇는 체육복 검사
    for r in reserve:
        
        if r == -99:
            continue
        
        flag = False
        # cal_num = 1
        for diff in [-1,1]: # +1, -1 검사
            # cal_num = -cal_num # 첫번째 turn: -1, 두번째 turn: +1
            find_num = r + diff
            
            if flag:
                continue
                
            
            if find_num in lost: # lost에 있다면
                count += 1
                lost[lost.index(find_num)] = -99 # 여기가 인덱스가 아니라 해당번호를 바꿔야해 # IndexError: list assignment index out of range
                
                flag = True
            
    
    return count


"""
1. lost랑 reverse에 중복되는애를 reverse에서 빼고
2. count는 중복된애를 제외한 reverse 길이에서 시작. reverse for문을 돌아가며 각 reverse 당 lost 조사 
3. reverse에서 -1, +1 했을때 Lost값이 있다면 - lost값 -99으로 처리하고 count+=1, 없다면 - 다음 reverse

[1,'2',3,4,'5',6]
"""
