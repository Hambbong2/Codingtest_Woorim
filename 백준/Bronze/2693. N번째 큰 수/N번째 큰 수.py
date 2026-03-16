T = int(input())

for _ in range(T):
    
    num_list = list(map(int, input().split()))
    
    num_list = sorted(num_list, key=lambda x: -x)
    
    print(num_list[2])