from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    numbers_str = list(map(str, numbers))
    
    def compare(x, y):
        
        if x+y < y+x:
            return 1 # 두 수를 바꿔
        elif x+y > y+x:
            return -1 # 두 수를 바꾸지마.
        else:
            return 0 # 두 수 안바꿔도 되는데 리턴값이 필요하니까 0으로 둘게
    numbers_str.sort(key=cmp_to_key(compare))
    # numbers_sort = numbers_str.sort(key = cmp_to_key(compare)) # 파이썬에서 **.sort()**는 원본 리스트를 그 자리에서(In-place) 정렬하고 끝납니다. 즉, 정렬된 리스트를 새로 만들어주는 게 아니라 None을 리턴해요. 
    answer = ''.join(numbers_str) #join함수는 리스트를 하나의 str로 합쳐주는 함수. 구분자는 '','-',','에 등등 다양함
    
    # 샤갈!!!! [0,0,0] 인 케이스를 어떻게 생각하는데? 진짜 짜증 제대로다.
    # [0,0,0,..] 이 오면 어쨌든 인덱스 0번째에 0이 온다는 것은 그 뒤에도 0이라는 것이다. 정렬 이후이기 때문에 그래서 그냥 다 0으로 처리한다.
    if answer[0] == '0': return '0'
    
    return answer

"""
샤갈의 눈 내리는 마을이다. cmp_to_key면 내가 어케 푸니
1. 첫째 자리가 가장 큰 순서 > 둘째 자리가 가장 큰 순서.. 우선순위가 있음
        이때 none값이 제일 크다. 3 > 30 
        
        분할 정복으로 풀어야 할듯
        97 964 90 9 775 74 4 46 2
        
        99796490 
        775 74
        446
        2
        
        0부터 9,none값을 한자리수마다 비교해가며 정렬할거림
        1. 첫번째 자리가 똑같은 애들끼리 정렬
            - 첫째 자리, 둘째 자리,.. 비교해가며 가장 큰 수가 정렬
            - 단 none값이 가장 크고 그리고 9,8,7,...0순으로 크다
        
        
        --
        1. 첫째 자리 수 조사 n, 딕셔너리에 저장 리스트로
        2. 딕셔너리에 군집별로 정렬
        3. 마지막 합쳐
"""