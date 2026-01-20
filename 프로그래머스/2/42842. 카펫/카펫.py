def solution(brown, yellow):
    answer = []
    total_num = brown + yellow
    
    for height in range(3, int(total_num**0.5)+1): #가로든 세로든 1이나 2이면 조건이 성립 안돼서 3부터 시작해야함.(brown, yellow 최솟값이 8, 1인거 고려하고)
        if total_num % height == 0:
            width = total_num // height
            
            avail_w = width - 2
            avail_h = height - 2
            
            if yellow != (avail_w * avail_h):
                continue
                
            answer.append(width)
            answer.append(height)
            break

    
    return answer

"""

for i in range(3, int(num**0.5)+1) # num이 36이라면, i는 3,4,5,6 반복문을 돈다.

<옐로우 인덱스에 0이 들어가면 안돼 - 0이 있는 거는 바깥에 있다는 거니까>
1. 브라운+옐로우 했을때 만들 수 있는 직사각형 경우의 수를 반복문을 돌아. 소수구할때 썼던 쌍조합이용
2. 대신 옐로우 인덱스 0이 들어가면 탈락, 통과하면 리턴

"""