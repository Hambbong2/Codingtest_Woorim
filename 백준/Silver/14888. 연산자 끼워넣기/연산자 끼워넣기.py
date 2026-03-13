N = int(input())
num_list = list(map(int,input().split()))
plus, mius, multiply, divide = map(int, input().split())
res_list = []

def dfs(cur_idx, res, plus, mius, multiply, divide):
    
    # 종료조건 
    if cur_idx >= N:
        res_list.append(res)
        return
    
    if plus > 0:
        # res = res + num_list[cur_idx]
        dfs(cur_idx+1, res + num_list[cur_idx] , plus-1, mius, multiply, divide)
    
    if mius > 0:
        # res = res - num_list[cur_idx]
        dfs(cur_idx+1, res - num_list[cur_idx] , plus, mius-1, multiply, divide)
    
    if multiply > 0:
        # res = res * num_list[cur_idx]
        dfs(cur_idx+1, res * num_list[cur_idx] , plus, mius, multiply-1, divide)
    
    if divide > 0: 
        
        dfs(cur_idx+1, int(res / num_list[cur_idx])
            , plus, mius, multiply, divide-1)
            
        


dfs(1, num_list[0], plus, mius, multiply, divide)

print(max(res_list))
print(min(res_list))
