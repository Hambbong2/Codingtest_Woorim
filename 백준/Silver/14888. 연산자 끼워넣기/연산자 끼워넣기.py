from itertools import permutations

N = int(input())
A_list = list(map(int, input().split())) # [1,2,3,4,5,6]
tool_num_list = list(map(int, input().split())) # ['+', '+', '-', '*', '/'] 

# 데이터 거꾸로 뒤집기 - 스택만들기
per_st_1 = []
for i in range(len(A_list)):
    per_st_1.append(A_list[-i-1])
    
# 연산자 리스트 만들기
# tool_list = ['+','-','*','/']

tool_list = []
for idx in range(4):
    
    if idx == 0:
        for _ in range(tool_num_list[0]):
            tool_list.append('+')
  
    
    elif idx == 1:
        for _ in range(tool_num_list[1]):
            tool_list.append('-')      


    elif idx == 2:
        for _ in range(tool_num_list[2]):
            tool_list.append('*')
    
    elif idx == 3:
        for _ in range(tool_num_list[3]):
            tool_list.append('/')

      
permutation = set(permutations(tool_list)) # set으로 중복제거
result = []

for per in permutation:
    # per_st 다시 초기화..어카지
    per_st = per_st_1[:]
    
    for cal in per:
        
        if per_st:
            
            if cal == '+':
                c1 = per_st.pop()
                c2 = per_st.pop()
                per_st.append(c1 + c2)
            elif cal == '-':
                c1 = per_st.pop()
                c2 = per_st.pop()
                per_st.append(c1 - c2)
            elif cal == '*':
                c1 = per_st.pop()
                c2 = per_st.pop()
                per_st.append(c1 * c2)
            elif cal == '/':
                c1 = per_st.pop()
                c2 = per_st.pop()
                
                if c1 < 0:
                    res = -c1 / c2
                    per_st.append(int(-res))
                    continue
                elif c1 == 0:
                    per_st.append(0)
                    continue
                
                per_st.append(int(c1 / c2))
    
    per_res = per_st.pop()
    result.append(per_res)


print(max(result))
print(min(result))
