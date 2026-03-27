def solution(message, spoiler_ranges):
    answer = 0
    """
    2. 스포 방지 구간이 아닌 곳에 또 나오면 안돼. - 그럴려면 스포방지 할 이유가 없으니 중요한게 아니겟지
    3. 동일하게 앞에서 이미 공개된 거면 안돼. (2번이랑 언제 등장하냐의 뜻)
    
    phone 010 may i phone number - 후보들
    후보들과(스포방지 후보들) / 후보가 아닌(스포방지 단어가 아닌것)
    동일하게 이미 앞에서 공개된 거면 제외
    """
    
    # 문자열 받기 
    # 문자열의 공백이 있으면 다음 공백까지 인덱스 처리, split(' ')
    normal_word = []
    special_word = []
    words = []
    curr = 0
    # [('here',0,3), ('is',5,6),...]
    for m in message.split():
        start_idx = message.find(m, curr)
        end_idx = start_idx + len(m) - 1
        words.append((m,start_idx, end_idx))
        curr = end_idx + 1
        
    

    for w, s, e in words:
        flag = False
        for start, end in spoiler_ranges:
            if not (e<start or s > end):
                flag = True
                break
        if flag:
            special_word.append(w)
        else:
            normal_word.append(w)
    
    
    # 3번 조건
    special_word = set(special_word)
    normal_word = set(normal_word) # 이후에 교집합 위함
    
    answer = len(special_word) - len(special_word.intersection(normal_word))
    

    
    
    return answer