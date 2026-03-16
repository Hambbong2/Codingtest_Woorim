num1, num2 = map(int, input().split())

# 최대공약수 (Greatest Common Divisor)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 (Least Common Multiple)
# 공식: (a * b) / 최대공약수
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(gcd(num1,num2))
print(lcm(num1, num2))
# import math

# a, b = 12, 18

# # 최대공약수
# print(math.gcd(a, b))  # 결과: 6

# # 최소공배수 (Python 3.9 이상에서 지원)
# print(math.lcm(a, b))  # 결과: 36