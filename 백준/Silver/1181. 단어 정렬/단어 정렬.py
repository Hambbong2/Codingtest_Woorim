
# N = int(input())

# alpabet_list = []
# res = []
# for _ in range(N):
#     a = input()
#     a_len = len(a)
#     alpabet_list.append((a, a_len)) # (문자열, 정수) # ("but", 3)

# # 중복제거
# alpabet_list = list(set(alpabet_list))

# # 정렬하기
# alpabet_list.sort(key = lambda s : s[1]) # lambda arguments:expression 이라는데 여기서 원소가 (str, int)가 아니라 그냥 x라고..?

# # 알파벳 순으로 정답 res에 넣기

# alpabet_len = set()
# for a in alpabet_list:
#     _, a_len = a
    
#     alpabet_len.add(a)
    

# for len_num in alpabet_len: # (1,2,3)
#     temp_list = [x[0] for x in alpabet_list if x[1] == len_num] # [i], [no,it]
    
#     # 알파벳순으로 정렬
#     temp_list.sort()
    
#     # 중복 제거
    
    
    
# print(*res, sep='\n')

    
N = int(input())

words = []
for _ in range(N):
    words.append(input())

# 1. 중복 제거 (set을 사용하면 리스트가 순서 없는 집합이 됨)
words = list(set(words))

# 2. 정렬 (핵심!)
# 파이썬은 튜플을 정렬할 때 앞의 요소부터 비교합니다.
# (길이, 단어) 형태로 정렬하면: 1순위 길이, 2순위 사전순 정렬이 한 번에 끝납니다.
words.sort(key=lambda x: (len(x), x))

# 3. 출력
# 이미 words가 정렬되었으므로 바로 출력하면 됩니다.
print(*words, sep='\n')