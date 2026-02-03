def solution(friends, gifts):
    
    # 친구들 딕셔너리
    friends_dict = {name: idx for idx, name in enumerate(friends)}
    
    # 두 관계 간 선물 주고 받은거 카운트
    N = len(friends)
    gifts_arr = [[0]*N for _ in range(N)] # row -> col : giver -> taken
    
    # 선물지수
    gifts_index = [0]*N
    
    # 다음달에 선물 받을 횟수
    next_receive = [0]*N
    
    # 데이터 반영 -> 여기 익숙하지 않음..ㅠ
    for g in gifts:
        giver, taker = g.split()
        g_idx, t_idx = friends_dict[giver], friends_dict[taker]
        
        gifts_arr[g_idx][t_idx] += 1
        
        gifts_index[g_idx] += 1
        gifts_index[t_idx] -= 1
    
    # 비교 및 결과
    for i in range(N):
        for j in range(i+1,N):
            
            if gifts_arr[i][j] > gifts_arr[j][i]:
                next_receive[i] += 1
            elif gifts_arr[i][j] < gifts_arr[j][i]:
                next_receive[j] += 1
            else: # 둘이 같을 때(0도 포함됨 자연스럽게)
                if gifts_index[i] > gifts_index[j]:
                    next_receive[i] += 1
                elif gifts_index[i] < gifts_index[j]:
                    next_receive[j] += 1
                else:
                    continue
    return max(next_receive)
                
