# en_dict = {}

# S = input() # 띄어쓰기 받을 수 잇나?
# count = 0
# while S != '':
#     temp = ''
#     for s in S:
        
#         if s == ' ':
#             if temp != '': # 마지막 단어 어케 포함시키지?
#                 if en_dict.get(temp,0) == 0: # 없는 단어
#                     en_dict[temp] = 1
#                 else:
#                     en_dict[temp] += 1
        
#                 temp = ''
#         else:
#             temp += s
    
#     if temp != '':
#         en_dict[temp] = en_dict.get(temp, 0) + 1

#     for _, v in en_dict.items():
#         count += v
#     break

# print(count)

"""
위에꺼 시간초과
"""
    
S = input()

words = S.split() # 앞뒤 공백 제거 + 중간의 여러 공백도 알아서 처리함 -> 맨뒤에 붙여있거나 맨앞에 있는 공백도 처리해?

en_dict = {}


for word in words:
    en_dict[word] = en_dict.get(word,0) + 1

print(sum(en_dict.values()))