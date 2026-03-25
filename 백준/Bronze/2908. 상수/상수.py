n1, n2 = map(str, input().split())

n1, n2 = int(n1[::-1]), int(n2[::-1])

print(max(n1,n2))