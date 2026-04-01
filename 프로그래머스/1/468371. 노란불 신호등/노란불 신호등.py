"""
- 모든 신호등: 초록불 → 노란불 → 빨간불 반복
- 신호의 지속 시간은 신호등마다 다릅니다.
- 시간은 1초부터 시작. 처음에는 초록불 상태로 시작

이 도로에서는 가끔 정전이 일어나는데, 모든 신호등이 모두 노란불이 되면 정전이 발생한다는 사실이 밝혀졌습니다.

** 모든 신호등이 노란불이 되는 가장 빠른 시각(초)을 return **
(만약 모든 신호등이 노란불이 되는 경우가 존재하지 않는다면 -1을 return)
"""

"""
DP 처럼 배열같은 스택에 넣기 - 크기 미리 지정하면 20*5 최대 100칸인가?
"""
import math

def solution(signals):
    answer = 0
    time_table = []
    
    # 시그널 G, Y, R 을 스택에 시간만큼 넣기
    for signal in signals:
        time = 0
        each_singals = []
        # each_singals.append(-1) # 0초 -> 1초씩 빠르게 시작
        for idx, s in enumerate(signal):
            color = idx % 3 # 0: 초, 1: 노, 2: 빨
            for _ in range(s):
                each_singals.append(color)
        time_table.append(each_singals)
        
    # 1초부터 노랑불 확인 
    """
    time_table = [
                [0,0,1,2,2], 
                [0,0,0,0,0,1,2]]
                ]
    """
    flag = True
    idx = 0 
    time = 0 # 시간은 0초가빠짐. 1초 빠름
    
    # [추가] 수학적인 종료 조건 설정: 모든 주기의 최소공배수(LCM)
    # 900000 대신 이 값까지만 확인하면 됩니다.
    lcm_val = len(time_table[0])
    for i in range(1, len(time_table)):
        p = len(time_table[i])
        lcm_val = (lcm_val * p) // math.gcd(lcm_val, p)
    
    while 1: # 매초마다
        flag = True
        compare_color = time_table[0][time%len(time_table[0])]
        
        if compare_color == 1:
        
            for idx in range(1,len(time_table)): # 각 시그널 확인
                cur_color = time_table[idx][time%len(time_table[idx])]

                if cur_color == 0 or cur_color ==2:
                    flag = False
                    break
        else:
            flag = False


        if flag:
            answer = time + 1
            break
        
        
        # 종료조건 어카지
        if time >= lcm_val:
            answer = -1
            break
        
        time +=1
        
    return answer
                
                
    