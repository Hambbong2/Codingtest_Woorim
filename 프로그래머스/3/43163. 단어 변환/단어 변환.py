"""
a b c d e f g h i g k l m n o p q r s t u v w x y z

--
주어진 words 안에서가 아니라 밖에서! 큐를 단어하나씩 넣는거임. 그리고 검사를 한글자만 같은지

앞으로 갈 곳을 저장할 q
    
while q  
    q에서 하나 빼기
    뺐으니까 방문!
    
    for q와 인접한 곳도 찾아볼까?
        if 만약에 방문안햇으면 (또는 다른 조건있으면~)
            방문할 목록 q에 넣어
            
"""
from collections import deque
def solution(begin, target, words):
    
    visited = [False] * (len(words)+1)
    
    words = [begin] + words
    
    start_idx = 0
    dist = 0
    queue = deque([(start_idx, dist)]) # (인덱스, 횟수)
    visited[start_idx] = True
    
    while queue:
        
        cur_idx, cur_dist = queue.popleft()
    
        cur_word = words[cur_idx]
        
        if cur_word == target:
            return cur_dist
        
        for idx, word in enumerate(words):
            if visited[idx] == False:
                same_cnt = 0 # 글자수가 동일한 개수
                for i in range(len(word)):
                    
                    if word[i] == cur_word[i]:
                        same_cnt += 1
                        
                if same_cnt == (len(word)-1):
            
                    queue.append((idx,cur_dist+1)) # 중요한게 거리를 queue에 같이 넣는다!
                    visited[idx] = True
    
    return 0