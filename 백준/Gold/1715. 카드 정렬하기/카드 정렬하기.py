"""
가장 작은 수대로 앞에 정렬하는게 좋다..?
"""
import heapq
import sys

input = sys.stdin.readline
N = int(input())
cards = []
res_list = 0
total_res = 0

for _ in range(N):
    
    heapq.heappush(cards, int(input())) # cards는 리스트

# 그리디
if len(cards) <= 1:
    print(0)
else:

    while len(cards) > 1:
        
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)

        res = first + second
        total_res += res
        heapq.heappush(cards, res)

    print(total_res)

# 10 20 30 40 50 60 
# 틀림!!! 매번 가장 작은 것끼리 더해야 한다. -> 이걸 어케 생각하노..

# for front in range(N-1):
#     temp_sum = card_num_list[front] + card_num_list[front+1]
#     res += temp_sum
#     card_num_list[front+1] = temp_sum
    