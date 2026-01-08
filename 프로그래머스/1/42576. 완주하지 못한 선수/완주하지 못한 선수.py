def solution(participant, completion):
    answer = ''
    hash_map = {}
    # 1. 참가자 해시맵 만들기(예외 동명이인 -> 이름별 '명'수를 카운트 )
    for name in participant:
        hash_map[name] = hash_map.get(name,0)+1
    
    # 2. 완주한 사람은 다시 -1 하기
    for name in completion:
        hash_map[name] -= 1
        
    # 3. 완주 못한 사람 찾기
    # 고유인: 참가 1 완주했으면 = 0, 완주안했으면 1
    # 동명이인: 참가 2이상, 완주x 1
    # 완주를 안하면 1보다 크다.
    
    for name in participant:
        if hash_map[name] > 0:
            return name
        
  