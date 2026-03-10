# num = 27
# binary_num = bin(num)

# print(binary_num)
# print(binary_num[2:])

# print(type(binary_num))
# print(format(27,'b'))

# def decimal_to_binary(n):
#     if n == 0:
#         return ""
    
T = int(input())

for _ in range(T):
    num = int(input())
    
    binary_num = bin(num)[2:]

    
    one_list = []
  
    for i in range(len(binary_num)):
        
        if binary_num[-i-1] == '1':
            one_list.append(i)
    
    print(*one_list)
    
    