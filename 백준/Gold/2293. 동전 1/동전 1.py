
n, k = map(int, input().split())

"""
한개만
두개만
세개만
"""
coin_list = []
for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

# 동전 문제의 정석 풀이 (DP)
dp = [0] * (k + 1)
dp[0] = 1 # 0원을 만드는 방법은 1가지 (아무것도 안 내기)

for coin in coin_list:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])