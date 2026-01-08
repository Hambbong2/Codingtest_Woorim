from collections import deque

def solution(priorities, location):
    answer = 0
    
  
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    
    sort_pri = sorted(priorities, reverse = True)
    queue_sort = deque(sort_pri)
    
    while queue:
        cur_process, idx = queue[0]
        
        if cur_process < queue_sort[0]:
            queue.popleft()
            queue.append((cur_process,idx)) # 원래 튜플형태니까 넣을때도 주의
        else:
            queue.popleft()
            queue_sort.popleft() # 빼는거 주의!!
            answer += 1 # 실행된 우선순위
            if idx == location:
                return answer
    
    return answer


# 아래는 헷갈렸던 원래 내 코드
# from collections import deque
# def solution(priorities, location):
    
#     copy_prior = priorities[:]
#     sort_pri = sorted(copy_prior, reverse= True)
#     check_list = [0] * len(priorities)
#     check_num = 0
#     idx = 0
    
#     queue = deque(priorities)
#     queue_sort = deque(sort_pri)
    
    
#     while queue:
#         # cur_process = queue.popleft() # 아 여기때문에 바보
#         cur_process = queue[0]
#         cur_idx = idx % len(copy_prior)
#         max_pri = queue_sort[0]
        
#         if cur_process < max_pri:
#             queue.popleft()
#             queue.append(cur_process)
#         else:
#             # 우선순위 가장 높은 프로세스이므로 실행
#             queue_sort.popleft()
#             queue.popleft()
#             check_num += 1
#             check_list[cur_idx] = check_num
            
        
#         idx += 1
        
# # idx     1 1 9 1 1 1
# #         ---
# #  0      1 9 1 1 1 1
        
# #  1      9 1 1 1 1 1
        
# #  2      1 1 1 1 1 - 9
        
# #  3      1 1 1 1 - 1
        
# #  4      1 1 1 - 1

# #  5      1 1 - 1

    
#     return check_list[location]
