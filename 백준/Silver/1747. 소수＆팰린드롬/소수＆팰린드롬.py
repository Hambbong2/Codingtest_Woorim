import sys

def is_prime(num):
    if num < 2: return False
    # 소수 판별의 핵심: 제곱근까지만 확인!
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    # 숫자를 문자열로 바꿔서 뒤집은 것과 비교
    s = str(num)
    return s == s[::-1]

# N 입력 받기
N = int(sys.stdin.readline())

target = N
while True:
    # 1. 먼저 팰린드롬인지 확인 (문자열 비교가 소수 판별보다 보통 더 빠름)
    if is_palindrome(target):
        # 2. 팰린드롬이라면 소수인지 확인
        if is_prime(target):
            print(target)
            break
    target += 1