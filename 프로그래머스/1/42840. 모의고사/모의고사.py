def solution(answers):
    answer = [0,0,0]
    length_ans = len(answers)
    p1 = [1,2,3,4,5] # 길이 5
    p2 = [2,1,2,3,2,4,2,5] # 길이 8
    p3 = [3,3,1,1,2,2,4,4,5,5] # 길이 10
    
    for idx in range(length_ans):
        
        if p1[idx % 5] == answers[idx]:
            answer[0] += 1
        
        if p2[idx % 8] == answers[idx]:
            answer[1] += 1
            
        if p3[idx % 10] == answers[idx]:
            answer[2] += 1
        
    # max 개수가 여러개라면
    max_score = max(answer)
    result = []
    
    for i in range(3):
        if answer[i] == max_score:
            result.append(i+1)
        
        
    return result
