"""
구간합(prefix Sum)문제다! 
"""

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

solv_list = []
prefix_sum = [[] for _ in range(B+1)]



#문제 배열 만들기
for num in range(B+1):
    
    if len(solv_list) > B+1:
        break
    
    if num == 0:
        solv_list.append(0)
        continue
    
    for _ in range(num):
        solv_list.append(num)

# 구간합 배열 만들기
for i in range(B+1):
    
    if i == 0:
        prefix_sum[i] = 0
        continue
    
    if i == 1:
        prefix_sum[i] = solv_list[1]
    else:
        prefix_sum[i] = prefix_sum[i-1] + solv_list[i]


print(prefix_sum[B]-prefix_sum[A-1])

