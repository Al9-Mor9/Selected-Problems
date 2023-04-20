import sys
sys.stdin = open("input.txt", "r")

# 10000이하 자연수 10 <= n <= 100,000 개 줌.
# 그리고 0 < S < 100,000,000 줌

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split())) + [0]

ans = N
left, right = 0, 1
sum = arr[0]
f = 0
while right < N + 1:
    if sum < S:
        sum += arr[right]
        right += 1
    else:
        f = 1
        sum -= arr[left]
        left += 1
        ans = min(ans, right - left)

if not f: 
    print(0)
    sys.exit()

print(ans + 1)
