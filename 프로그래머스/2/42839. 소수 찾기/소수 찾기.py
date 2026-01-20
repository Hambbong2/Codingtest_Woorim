from itertools import permutations
def solution(numbers):
    answer = set()
    num_list = list(numbers) # ['1', '7'] 문자열 리스트
    
    for length in range(1, len(num_list)+1):
        for p in permutations(num_list, length): # permutations: 순열, (반복가능한 객체, 길이)
            
            num_p = int(''.join(p))
            # join은 반복가능한 객체인데 문자열일 때 사용 # p가 int형이면 이렇게 바꿔야함. ''.join(map(str,p))
            if is_prime(num_p):
                
                answer.add(num_p)
                
    return len(answer)

def is_prime(num):
    
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    