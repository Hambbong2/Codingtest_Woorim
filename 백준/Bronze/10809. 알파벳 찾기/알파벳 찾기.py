alphbet = [-1] * 26

input_str = input()

for idx, s in enumerate(input_str):
    
    if alphbet[ord(s)-ord('a')] == -1:
        alphbet[ord(s)-ord('a')] = idx

print(*alphbet)