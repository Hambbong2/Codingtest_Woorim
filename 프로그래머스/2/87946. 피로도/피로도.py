from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    num = len(dungeons)
    duns_com = permutations(dungeons,num)
    
    for com in duns_com:
        k_temp = k
        cnt = 0
        for min_hp, end_hp in com: # 특정 조합
            
            if k_temp >= min_hp:
                k_temp -= end_hp
                cnt += 1
        
        answer = max(cnt, answer)
            
            
    return answer

"""
최소피로도는 높을수록, 소모 피로도는 낮을수록 좋은건가?
근데 우선순위는 최소피로도가 ... 음 그런거 말고 순열을 이용해서 가장 큰 값 찾아얗ㄱ
"""