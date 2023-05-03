import sys
sys.stdin = open('input.txt', 'r')
#####
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
ans = 0
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y):
    # memoization
    if dp[x][y]:
        return dp[x][y]

    # 현 위치 1부터 시작
    dp[x][y] = 1

    # delta
    for dx, dy in dr:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)