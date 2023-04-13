import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    while b: a, b = b, a%b
    return a

f_gcd, b_gcd = [0] * n, [0] * n 
f_gcd[0], b_gcd[-1] = arr[0], arr[-1]

for i in range(1, n - 1):
    f_gcd[i] = gcd(f_gcd[i - 1], arr[i])

for i in range(n - 2, 0, -1):
    b_gcd[i] = gcd(arr[i], b_gcd[i + 1])

idx = 0 
max_ = b_gcd[1]
for i in range(1, n - 2):
    tmp = gcd(f_gcd[i - 1], b_gcd[i + 1])
    if tmp > max_:
        max_ = tmp
        idx = i

if max_ < f_gcd[-2]:
    max_ = f_gcd[-2]
    idx = n

print(max_, arr[idx] if arr[idx] % max_ else -1)