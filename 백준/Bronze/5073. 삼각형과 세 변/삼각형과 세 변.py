import sys

input = sys.stdin.readline
res = []

while True:
    
    l1, l2, l3 = map(int, input().split())

    # 입력받기 0 0 0이 나올 때까지    
    if l1 == 0 and l2 == 0 and l3 == 0:
        break
    
    
    # 삼각형 조건을 만족하지 못할 때

    max_len = max(l1, l2, l3)
    min_len = min(l1, l2, l3)
    
    rest_len = (l1+l2+l3) - (max_len + min_len)
    
    if max_len >= min_len + rest_len:
        res.append('Invalid')
        continue
    
    if max_len == min_len == rest_len:
        res.append('Equilateral')
        continue
    
    elif max_len == min_len or max_len == rest_len or min_len == rest_len:
        res.append('Isosceles')
        continue
    
    # 세 변의 길이가 다른 경우
    elif (max_len != min_len) and (max_len != rest_len) and (min_len != rest_len):
        res.append('Scalene')

print(*res, sep='\n')