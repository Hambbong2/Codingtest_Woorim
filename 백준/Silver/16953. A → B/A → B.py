
A, B = map(int, input().split())

min_count = float('inf')

def back_tracking(num, count):
    global min_count
    # 종료조건
    if num == B:
        min_count = min(min_count, count)
        return
    
    if num > B:
        return
    
    back_tracking(num*2, count+1)
    
    back_tracking(num*10+1, count+1)
    
    # 34가 341이     
    

back_tracking(A,0)

if min_count != float('inf'): # 이거 랜덤값아님? no -> 파이썬은 이를 무한대라 생각. 어떤 수를 가져와도 항상 크고,
    print(min_count+1)
else:
    print(-1)    
    
    
"""
999조 < float('inf') → True

float('inf') == float('inf') → True (항상 똑같은 '무한대' 상태입니다.)
"""
 