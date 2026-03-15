import sys


input = sys.stdin.readline

M = int(input())
N = int(input())

prime_list = []

def is_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2,int(num**(0.5))+1):
        
        if num % i == 0: # 약수일 떄
            return False

    return True


for num in range(M, N+1):
    
    if is_prime(num):
        prime_list.append(num)
    

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)