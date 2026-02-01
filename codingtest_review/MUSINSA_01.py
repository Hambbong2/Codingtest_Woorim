
# """
# 브랜드마다 사이즈가 다르다.
# 하지만 허리, 가슴, 엉덩이 파트는 꼭 들어간다.

# - 딕셔너리로 저장하는 것
# - 찾는 것

# 입력
# 2 1 # 브랜드 수, 고객 수
# nike 3 # 브랜드명, 사이즈 개수
# nike S 150,160,80,90,45,50 # 브랜드명, 사이즈 정보(허리, 가슴, 엉덩이)
# nike M 150,160,80,90,45,50 # 브랜드명, 사이즈 정보(허리, 가슴, 엉덩이)
# nike L 150,160,80,90,45,50 # 브랜드명, 사이즈 정보(허리, 가슴, 엉덩이)

# nike 158, 80, 45 # 고객이 원하는 브랜드명, 사이즈 정보(허리, 가슴, 엉덩이)


# brands_dict ={
#     'nike': {
#         H: [(150,160), (160,170), (170,180)]
#         C: []
#         W: []
#     },
    
#     'adidas': {
#         ...
#     }
    
# }
# """
# brands_dict = {}
# brands_size = {}

# B, Q = map(int,input().split())

# # 브랜드들의 딕셔너리 만들기
# for _ in range(B):
    
#     S, N = map(int,input().split())
#     brands_dict[S] = {
#         'H': [],
#         'C': [],
#         'W': []
#     }
    
#     # part별로 넣기
#     for _ in range(N):
#         name, size, H_min, H_max, C_min, C_max, W_min, W_max = map(int, input().split())
#         brands_dict[S]['H'].append((H_min, H_max)) # key 대로 어떻게 넣지 #튜플도 min, max되나
#         brands_dict[S]['C'].append((C_min, C_max))
#         brands_dict[S]['W'].append((W_min, W_max))
        
#         brands_size[name].append(size) # 이러면 자동으로 리스트형태로 추가임? 꼭 key:value가 1:1인가?

# # 고객 요청 받고 알맞는 브랜드와 사이즈 추천하기
# for _ in range(Q):
#     client_brand, client_h, client_c, client_w = map(int, input().split())
    
#     if brands_dict.get(client_brand,0) == 0:
#         print('UNKNOWN')
#         continue
    
#     # 모두 최댓값보다 높으면 UP, 모든 최솟값보다 작으면 DOWN, 섞여있으면 unmatched 출력
#     H_match = []
#     C_match = []
#     W_match = []
    
#     # 허리
#     for idx, (H_min, H_max) in enumerate(brands_dict[client_brand]['H']):
#         if H_min <= client_h <= H_max:
#             H_match.append(idx)
#             break
#         elif client_h < H_min:
#             H_match = -1
#         else:
#             H_match = -2
            
#     # 가슴
#     for idx, (C_min, C_max) in enumerate(brands_dict[client_brand]['C']):
#         if C_min <= client_c <= C_max:
#             C_match.append(idx)
#             break
#         elif client_c < C_min:
#             C_match = -1
#         else:
#             C_match = -2
            
#     # 엉덩이
#     for idx, (W_min, W_max) in enumerate(brands_dict[client_brand]['W']):
#         if W_min <= client_w <= W_max:
#             W_match.append(idx)
#             break
#         elif client_w < W_min:
#             W_match = -1
#         else:
#             W_match = -2

#     if H_match == -1 and C_match == -1 and W_match == -1:
#         print('DOWN')
#     elif H_match == -2 and C_match == -2 and W_match == -2:
#         print('UP')
#     else:
#         possible_sizes = set(H_match) & set(C_match) & set(W_match)
#         if possible_sizes:
#             ?


import sys
input = sys.stdin.readline

brands = {}

B, Q = map(int, input().split())

# ---------- 브랜드 입력 ----------
for _ in range(B):
    brand, N = input().split()
    N = int(N)

    brands[brand] = {
        "sizes": [],   # 인덱스 = 사이즈(S,M,L,...)
        "H": [],       # 허리
        "C": [],       # 가슴
        "W": []        # 엉덩이
    }

    for _ in range(N):
        bname, size, H_min, H_max, C_min, C_max, W_min, W_max = input().split()
        H_min, H_max, C_min, C_max, W_min, W_max = map(int,
            [H_min, H_max, C_min, C_max, W_min, W_max]
        )

        brands[brand]["sizes"].append(size)
        brands[brand]["H"].append((H_min, H_max))
        brands[brand]["C"].append((C_min, C_max))
        brands[brand]["W"].append((W_min, W_max))


# ---------- 매칭 함수 ----------
def match_range(ranges, value):
    # -1 : DOWN, -2 : UP, index : 정상 매칭
    if value < ranges[0][0]:
        return -1
    if value > ranges[-1][1]:
        return -2

    for i, (mn, mx) in enumerate(ranges):
        if mn <= value <= mx:
            return i
    return None


# ---------- 고객 처리 ----------
for _ in range(Q):
    client_brand, client_h, client_c, client_w = input().split()
    client_h, client_c, client_w = map(int, [client_h, client_c, client_w])

    if client_brand not in brands:
        print("UNKNOWN")
        continue

    H_match = match_range(brands[client_brand]["H"], client_h)
    C_match = match_range(brands[client_brand]["C"], client_c)
    W_match = match_range(brands[client_brand]["W"], client_w)

    flags = [H_match, C_match, W_match]

    # 전부 DOWN
    if all(f == -1 for f in flags):
        print("DOWN")

    # 전부 UP
    elif all(f == -2 for f in flags):
        print("UP")

    # 전부 정상 매칭
    elif all(isinstance(f, int) and f >= 0 for f in flags):
        if H_match == C_match == W_match:
            size_name = brands[client_brand]["sizes"][H_match]
            print(client_brand, size_name)
            # 예시 출력: nike M
        else:
            print("UNMATCHED")

    # 섞여있으면
    else:
        print("UNMATCHED")
