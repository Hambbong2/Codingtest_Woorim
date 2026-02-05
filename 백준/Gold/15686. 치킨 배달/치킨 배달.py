N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 좌표 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

answer = float('inf')
selected = []

def dfs(start):
    global answer
    
    # M개 선택 완료
    if len(selected) == M:
        total = 0
        # 도시 치킨 거리 계산
        for hx, hy in houses:
            dist = float('inf')
            for idx in selected:
                cx, cy = chickens[idx]
                d = abs(hx - cx) + abs(hy - cy)
                if d < dist:
                    dist = d
            total += dist
        
        if total < answer:
            answer = total
        return
    
    # 조합 생성
    for i in range(start, len(chickens)):
        selected.append(i)
        dfs(i + 1)
        selected.pop()

dfs(0)
print(answer)
