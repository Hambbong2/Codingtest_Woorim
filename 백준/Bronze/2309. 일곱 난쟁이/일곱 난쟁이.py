"""
백트래킹 - 어느 조건에 백해야하는거지
조합 - 7명이라 고정되어잇으니까 시간복잡도는 어케 되는거지 7!..
"""

from itertools import combinations

# nine_list = list(map(int,input().split()))
nine_list = []

for _ in range(9):
    n = int(input())
    nine_list.append(n)

com_to_seven = combinations(nine_list, 7)

for com in com_to_seven:
    
    if sum(com) == 100:
        com = sorted(com)
        print(*com, sep='\n')
        break