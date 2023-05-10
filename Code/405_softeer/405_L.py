import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 인풋이 거지같아서 그렇지 그렇게 어렵진 않은듯
# 근데 이게 왜 디피임?

INF = int(2e5)
k, n = map(int, input().split())
cur = [0 for _ in range(k)]
jump = INF

for i in range(n):
    cost = list(map(int, input().split()))
    tmp = min(cur) + jump
    for g in range(k):        
        cur[g] = min(cur[g], tmp) + cost[g]

    if i == n-1: break
    jump = cost[-1]

print(min(cur))
