from itertools import product

def solution(clothes):
    """
    1. 문제처럼 옷장 딕셔너리 만들고, value를 튜플로 {
    "headgear" : ["","yellow_hat", "green_turban"],
    "headgear" : ["", "green_turban"],
    
    }
    2. 각 종류 별로 "" 빈 값을 추가했으니까 모두다 빈값인 경우(1가지)를 제외하고 갯수를 세면 됨
    예시) ["", ""], ["","blue_sungladdess"], ["yellow_hat",""], ["yellow_hat","blue_sunglasses"], ["green_turban", ""],  ["green_turban", "blue_sunglassess"] 에서 ["",""] 제외
    """
    
    clothes_dict = {}
    for c in clothes:
        
        if clothes_dict.get(c[1],0): # 딕셔너리에 이미 있는 key였으므로 그냥 추가
            clothes_dict[c[1]] += 1
        else: # 딕셔너리에 없었으면 리스트 만들고 추가
            clothes_dict[c[1]] = 2
    
    res = 1
    for v in clothes_dict.values():
        res = res*v 
#     values_list = list(clothes_dict.values()) # 이거의 출력 결과는?
#     drawers = product(*values_list)
    
#     answer = len(list(drawers)) - 1

    
    
    return res - 1
    