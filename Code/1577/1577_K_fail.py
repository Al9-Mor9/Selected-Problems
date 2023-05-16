# 도로의 개수(맞왜틀?)

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]
forbidden = []

for _ in range(K):
    a, b, c, d = map(int, input().split())
    if (a, b) < (c, d):
        forbidden.append((a, b, c, d))
    else:
        forbidden.append((c, d, a, b))

# dp 배열 초기화
dp[0][0] = 1
flag = 1
# 초반 위, 왼쪽이 모두 막힘
if (0, 0, 0, 1) in forbidden and (0, 0, 1, 0) in forbidden:
    flag = 0
# 초반 왼쪽이 막힘
elif (0, 0, 0, 1) in forbidden:
    for i in range(N+1):
        dp[i][0] = 1
# 초반 위쪽이 막힘
elif (0, 0, 1, 0) in forbidden:
    for j in range(M+1):
        dp[0][j] = 1
else:
    for i in range(N+1):
        dp[i][0] = 1
    for j in range(M+1):
        dp[0][j] = 1

if flag == 1:
    for i in range(1, N+1):
        for j in range(1, M+1):
            # 위, 왼쪽이 모두 막힘
            if (i, j-1, i, j) in forbidden and (i-1, j, i, j) in forbidden:
                dp[i][j] = 0
            # 왼쪽만 막힘
            elif (i, j-1, i, j) in forbidden:
                dp[i][j] = dp[i-1][j]
            # 위쪽만 막힘
            elif (i-1, j, i, j) in forbidden:
                dp[i][j] = dp[i][j-1]
            # 모두 뚫려있음
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][M])