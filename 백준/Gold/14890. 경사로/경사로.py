"""

가로 검사
    - (위에서 아래 검사)
    - (아래에서 위에 검사)
세로 검사

    - (위에서 아래 검사)
    - (아래에서 위에 검사)

"""
import sys

input = sys.stdin.readline
N, L = map(int, input().split())

def check(line, L):
    placed = [False] * len(line)
    
    
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            continue # s높이가 같으면 패스
        
        if abs(line[i] - line[i+1]) > 1:
            return False # 높이 차이가 1보다 클 때 실패
        
        if line[i] > line[i+1]:
            temp = line[i+1]
            for j in range(i+1, i+1+L):
                
                # line안에 들어가는지
                if 0 <= j < len(line):
                    if line[j] != temp or placed[j]:
                        return False
                    placed[j] = True # 경사로 설치
                else: 
                    return False
        
        elif line[i] < line[i+1]:
            temp = line[i]
            for j in range(i,i-L,-1): # 여기 길이 주의
                
                if 0<= j < len(line):
                    if line[j] != temp or placed[j]:
                        return False
                    placed[j] = True
                else:
                    return False
    return True



board = []
for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)

ans = 0
# 가로 검사
for row in board:
    if check(row,L):
        ans += 1
# 새로 검사
for c in range(N):
    # col = board[c][:] 이거 아님
    col = [board[r][c] for r in range(N)]
    if check(col, L):
        ans += 1
    

print(ans)