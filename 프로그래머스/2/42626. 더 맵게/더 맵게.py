# from heapq import heappush, heappop, heapify 이 미친 이게 from heapq할때나 import heapq할때랑 다른거죠 
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        
        if len(scoville) > 1:
            answer += 1
            sp1 = heapq.heappop(scoville)
            sp2 = heapq.heappop(scoville)
            
            temp = sp1 + (sp2*2)
            heapq.heappush(scoville, temp)
        else: 
            answer = -1
            break
    
# 아래꺼는 비효율적이라 런타임오류래 샤갈!!
#     while len(scoville) > 1:
#         # 1. k 만큼 매워질때 리턴
#         # 2. scoville pop할게 없을때 -1
        
#         min_sp = scoville[0]
        
#         if min_sp < K:
            
#             if len(scoville) == 1:
#                 answer = -1
#                 break
            
#             answer += 1
#             spicy_1 = heapq.heappop(scoville)
#             spicy_2 = heapq.heappop(scoville)

#             temp = spicy_1 + (spicy_2 * 2)
#             heapq.heappush(scoville, temp)


    return answer