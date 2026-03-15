bar_dict = {')': '(', ']': '['}

def check_bar(test_case):
    stack = []
    res = 0      # 최종 합계 (덧셈용)
    tmp = 1      # 현재 괄호 깊이에 따른 몸값 (곱셈용)
    
    for i in range(len(test_case)):
        ch = test_case[i]
        
        if ch == '(':
            stack.append(ch)
            tmp *= 2  # 몸값 2배 예약
        elif ch == '[':
            stack.append(ch)
            tmp *= 3  # 몸값 3배 예약
            
        elif ch == ')':
            # 에러 처리: 비어있거나 짝이 안 맞으면 0
            if not stack or stack[-1] != '(':
                return 0
            
            # [핵심 분기] 바로 전 글자가 여는 괄호였다면 '알맹이'다!
            if test_case[i-1] == '(':
                res += tmp  # 수확(더하기)
                
            stack.pop()
            tmp //= 2  # 영향력이 끝났으니 다시 나눔
            
        elif ch == ']':
            # 에러 처리
            if not stack or stack[-1] != '[':
                return 0
            
            # [핵심 분기] 바로 전 글자가 여는 괄호였다면 '알맹이'다!
            if test_case[i-1] == '[':
                res += tmp  # 수확(더하기)
                
            stack.pop()
            tmp //= 3  # 영향력이 끝났으니 다시 나눔
            
    # 스택에 괄호가 남았다면 0, 아니면 최종 합계 반환
    return res if not stack else 0

str_input = input()
print(check_bar(str_input))