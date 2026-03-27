import sys

n_8 = sys.stdin.readline().strip()

if n_8 == '0':
    print(0)
    exit()
bin_list = ["000", "001", "010", "011", "100", "101", "110", "111"]

result = []
first_digit = int(n_8[0])
result.append(bin(first_digit)[2:])
for i in range(1, len(n_8)):
    digit = int(n_8[i])
    result.append(bin_list[digit])
print("".join(result))