T = int(input())

for _ in range(T):
    R, n_str = map(str, input().split())
    P = ''
    for s in n_str:
        P = P + s*int(R)
    
    print(P.strip())