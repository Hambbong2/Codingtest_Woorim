def solution(s):
    answer = True
    st = [] # 스택을 ((( 방향만 쓰는거야!
    
    for char in s:
        if char == '(': # ( 일때
            st.append(char)
        else: # ) 일때
            
            if not st:
                answer = False
                break
            
            st.pop()
    
    if len(st) != 0:
        answer = False
        
    return answer