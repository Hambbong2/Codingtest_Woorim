def solution(n, wires):
    answer = 101
    
    def dfs(graph,w1,w2,visited,count):
        visited[w1] = True
        count = 1 # count += 1
        
        for i in graph[w1]:
            if not visited[i] and i != w2:
                count += dfs(graph, i, w2, visited,count)
        return count
        
    # 연결리스트 구현
    # link_list = [] * (n+1) # IndexError: list index out of range
    link_list = [[] for _ in range(n+1)]
    
    for w1, w2 in wires:
        link_list[w1].append(w2)
        link_list[w2].append(w1)
        
    
    # 연결리스트 하나씩 끊기
    for remove_w1, remove_w2 in wires:
        visited = [False] * (n+1)
        count = 0
        count = dfs(link_list, remove_w1, remove_w2, visited, count)
        
        sub_num = abs(count - (n - count))
        answer = min(answer, sub_num)
        
        
    
    return answer

"""
- 연결리스트로 구현하고 
- 하나씩 연결을 끊어(연결리스트에서 1과 5가 연결된다 하면 1-5, 5-1 를 없앤다)
- DFS로 몇개인지 확인한다.(나머지는 전체에서 BFS 구한거를 뺀다. 간선 하나를 없애는 거니까 하나의 집합을 DFS로 구하고 나머지는 그 나머지로 해도 문제가 없다. n개의 송전탐이 전선을 통해 모두 연결되었다 햇으니까..)
- 그중 차이가 가장 적은게 답


1 - 2
2 - 1, 3
3 - 2, 4
4 - 3

1 - 2
2 - 1, 7
3 - 4, 7
4 - 3, 5
5 - 4
6 - 7
7 - 2, 3, 6
"""