import sys

input = sys.stdin.readline
N, M = map(int, input().split())

"""
8*8 체스판에는 32개의 흰색과 32개의 검은색을 둘 수 있다.
"""

board = []
for _ in range(N):
    temp = input()
    board.append(temp)    


final_min = float('inf')

for i in range(N-8+1):
    for j in range(M-8+1):
        # 8x8 영역을 선택했을 때, 두 가지 경우를 모두 계산해봅니다.
        count_B = 0 # 맨 왼쪽 위가 'B'여야 하는 경우의 수정 횟수
        count_W = 0 # 맨 왼쪽 위가 'W'여야 하는 경우의 수정 횟수
        
        for r in range(8):
            for c in range(8):
                # 현재 칸의 위치가 (행+열)이 짝수인지 홀수인지에 따라 색이 결정됨
                if (r + c) % 2 == 0:
                    # 짝수 칸일 때
                    if board[i+r][j+c] != 'B': count_B += 1
                    if board[i+r][j+c] != 'W': count_W += 1
                else:
                    # 홀수 칸일 때 (짝수 칸과 반대 색이어야 함)
                    if board[i+r][j+c] != 'W': count_B += 1
                    if board[i+r][j+c] != 'B': count_W += 1
        
        # 8x8 판 하나가 끝날 때마다, 전체 최솟값을 갱신합니다.
        # 이번 8x8 판에서 나온 결과(count_B, count_W) 중 작은 것을 
        # 지금까지의 전체 최솟값(final_min)과 비교!
        final_min = min(final_min, count_B, count_W)

print(final_min)