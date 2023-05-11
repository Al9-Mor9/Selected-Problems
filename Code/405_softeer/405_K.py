# 복잡한 조립라인 2
import sys
sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())
dp = []     # (i, j)까지 가장 짧은 조립 시간
move = []   # 다른 라인으로 넘어가는 이동 시간

# 입력 처리
for i in range(N-1):
    line = list(map(int, input().split()))
    dp.append(line[:K])
    move.append(line[-1])
dp.append(list(map(int, input().split())))

for i in range(N-1):
    tmp = min(dp[i])    # 해당 열에서 가장 짧은 작업 시간
    for j in range(K):
        dp[i+1][j] += min(dp[i][j], tmp + move[i])

print(min(dp[-1]))









# --------------------------------------------------------------
# def dfs(sm, currow, cnt, N):
#     global ans
#     if sm >= ans:
#         return
#     if cnt == N:
#         ans = min(ans, sm)
#         return
#     for i in range(K):
#         if currow == i:
#             dfs(sm + line[i][cnt], i, cnt+1, N)
#         else:
#             dfs(sm + line[i][cnt] + move[cnt], i, cnt+1, N)

# K, N = map(int, input().split())    # 3 7
# line = [[0] * N for _ in range(K)]  # 작업 시간
# move = [0]   # 다른 행으로의 이동시간
# ans = 2e7

# for j in range(N-1):
#     *args, t = map(int, input().split())
#     move.append(t)
#     for i in range(K):
#         line[i][j] = args[i]

# last = list(map(int, input().split()))

# for i in range(K):
#     line[i][-1] = last[i]

# dfs(0, -1, 0, N)
# print(ans)