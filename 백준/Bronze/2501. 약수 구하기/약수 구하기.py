"""
약수란, 정의를 먼저 정의해라.
문제에선 자연수 p, q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
라고 한다.
"""

import sys

# ()를 붙이면 함수를 실행한 '결과(빈 문자열)'가 저장됩니다.
# 함수 그 자체를 별명으로 쓰려면 괄호 없이 대입해야 합니다.
input = sys.stdin.readline #sys.stdin.readline()  

N, K = map(int, input().split())

count = 0
i = 1 # 주의. 0으로 못나눔
while count < K:
    
    if N < i:
        print(0)
        break
    
    if N % i == 0:
        count += 1
        
        if count == K:
            print(i)
        
        
    i += 1
    