submit = [False] * 31

for _ in range(28):
    temp_idx = int(input())
    submit[temp_idx] = True

for idx in range(1,31):
    if not submit[idx]:
        
        print(idx)
    
