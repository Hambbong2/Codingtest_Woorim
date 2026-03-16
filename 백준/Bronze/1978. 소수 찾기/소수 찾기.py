num = int(input())
num_list = list(map(int, input().split()))
cnt = 0
def is_prime(num):
    
    if num <= 1:
        return False
    
    for i in range(2,int(num**(0.5))+1):
        
        if num % i == 0:
            return False
                
    
    return True


for n in num_list:
    
    if is_prime(n):
        cnt += 1

print(cnt)


            