import heapq
import sys

input = sys.stdin.readline
N = int(input())
origin_list = list(map(int, input().split()))

# 1. 중복을 제거한 값들만 힙에 넣습니다. (서로 다른 좌표 개수만 중요하니까!)
unique_nums = list(set(origin_list))
heapq.heapify(unique_nums)

# 2. 힙에서 하나씩 빼면서 "숫자: 순위" 딕셔너리를 만듭니다.
# 힙에서 처음 나온 놈이 0등, 그다음이 1등...
compressed_dict = {}
rank = 0
while unique_nums:
    num = heapq.heappop(unique_nums)
    compressed_dict[num] = rank
    rank += 1

# 3. 원래 리스트의 순서대로 딕셔너리에서 순위를 찾아 출력합니다.
for x in origin_list:
    print(compressed_dict[x], end=' ')