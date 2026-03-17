from itertools import permutations

N, M = map(int, input().split())

per_list = []


for num in range(1, N+1):
    per_list.append(num)
    
per = list(permutations(per_list, M))

for p in per:
    print(*p)