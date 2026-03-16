H, W = map(int, input().split())
W_list = list(map(int, input().split()))

water_cnt = 0

for idx in range(1, W-1):
    
    cur_W = W_list[idx]
    
    left = max(W_list[:idx])
    right = max(W_list[idx+1:])
    
    min_W = min(left, right)
    max_W = max(left,right)
    
    if cur_W < min_W:
        water_cnt += min_W - cur_W


print(water_cnt)