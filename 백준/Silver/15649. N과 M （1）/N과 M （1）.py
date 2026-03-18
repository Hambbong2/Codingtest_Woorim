# from itertools import permutations

# N, M = map(int, input().split())

# per_list = []


# for num in range(1, N+1):
#     per_list.append(num)
    
# per = list(permutations(per_list, M))

# for p in per:
#     print(*p)
########################################## 
N, M = map(int, input().split())
visited = [False] * (N + 1)  # 중복 선택 방지
result = []

def solve(depth):
    if depth == M:  # M개를 다 뽑았을 때 (기저 조건)
        print(*result)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True  # 방문 처리 (선택)
            result.append(i)
            
            solve(depth + 1)   # 다음 숫자 뽑으러 가기 (재귀)
            
            result.pop()       # 돌아와서 마지막 숫자 빼기 (후퇴)
            visited[i] = False # 방문 해제 (후퇴)

solve(0)