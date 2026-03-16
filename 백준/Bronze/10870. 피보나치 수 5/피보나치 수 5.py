# N = int(input())

# fibo_list = [0] * max(1,(N+1)) 
# fibo_list[0] = 0
# fibo_list[1] = 1
# """ 
# [[] for _ in range(N+1)]로 하면
# 빈곳이 0이 아니라 [] 리스트로 남는다.
# 그래서 탑다운으로 계산할때 값이 없으면 typeerror 가능성
# 어차피 숫자가 될 줄 알면, 0으로 미리 채워넣는다.

# 그리고 N이 1인경우도 생각해서 
# fibo_list = [[0], [1], [], []..]로 미리 채우면 안된다.
 

# """

# def fibo_cal(num):
    
#     if num == 0:
#         return 0
    
#     if num == 1:
#         return 1
    
#     for i in range(2, N+1):
#         fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    
#     return fibo_list[num]

# print(fibo_cal(N))

import sys

N = int(input())
memo = [-1] * (N+1)

def fibonacci_best_recursive(num):
    
    if num <= 1:
        return num
    
    if memo[num] != -1:
        return memo[num]
    
    memo[num] = fibonacci_best_recursive(num-1) + fibonacci_best_recursive(num-2)
    return memo[num]

print(fibonacci_best_recursive(N))