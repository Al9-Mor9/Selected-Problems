import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# ----------------------------------------------
# 첫 번째 줄에 사람 수 n과 버스에 태울 수 있는 사람 수 k가 주어진다. (1 ≤ k ≤ n ≤ 1000)
# 두 번째 줄에 n개의 정수 xi (i = 1, 2, ... , n, 1 ≤ xi ≤ n) 가 순서대로 주어진다. 
# xi는 xi번째 사람이 버스에 타지 않는다면 i번째 사람 역시 버스에 타지 않음을 의미한다.

# Strongly Connected Component 를 찾는 Tarjan's Algorithm
# 영서가 가면 하림이도 간다고 하자..

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr_r = [[] for _ in range(n + 1)]              # 반대 인접 리스트


visited1 = [0 for _ in range(n + 1)]
visited2 = [0 for _ in range(n + 1)]

SCC_min_max = [[0, 0] for _ in range(n + 1)]
SCC = []

# i가 mt에 가면, 간다고 할 놈들 
for i in range(1, n + 1):
    arr_r[arr[i]].append(i)

# print(arr)      # [0, 2, 3, 4, 5, 6, 7, 4, 7, 8, 8, 12, 12]
# print(arr_r)    # [[], [], [1], [2], [3, 7], [4], [5], [6, 8], [9, 10], [], [], [], [11, 12]]


def scc_root_dfs(SCC_NUM, cur):
    visited2[cur] = 1
    SCC_min_max[SCC_NUM][1] += 1      # 해당 SCC(싸이클)가 가면, 갈 수 있는 총 인원

    for naga in arr_r[cur]:           # 영서가 가면 갈 놈들...
        if not visited2[naga]:
            scc_root_dfs(SCC_NUM, naga)
    return

def dfs(cur, trace):
    visited1[cur] += 1

    if visited1[arr[cur]] > 0:              # 선행 조건이 만족 했다면, (영서가 갔다면.) 
        if arr[cur] in trace:               # 싸이클이 처음으로 발견 될 때, 
            s_idx = trace.index(arr[cur])   # 해당 싸이클만 뽑아보자.
            scc_elements = trace[s_idx:]    # 

            SCC.append(arr[cur])            # SCC에는 루트만 들어간다.
            SCC_num = len(SCC)              # 몇 번째 SCC인지 기록.

            SCC_min_max[SCC_num][0] = len(scc_elements) # 싸이클은 포함해야함.(그 무리...)
            scc_root_dfs(SCC_num, arr[cur])             # 그 무리가 포함될 경우 최대 몇 명까지 올 수 있는지 찾으러감.

    else:                           # 영서가 아직 안감.
        visited1[arr[cur]] += 1     # 먼저 보내고 영서의 선행조건 살피러감.
        trace.append(arr[cur])
        dfs(arr[cur], trace)


for i in range(1, n + 1):
    if not visited1[i]:
        dfs(i, [i])

# print(SCC)            # [4, 12]
# print(SCC_min_max)    # [[0, 0], [4, 10], [1, 2], [0, 0], ...] 
SCC_min_max = SCC_min_max[1:]


# dp 일반 냅색.
dp = [[0 for _ in range(k + 1)] for _ in range(len(SCC_min_max) + 1)]
for i in range(1, len(SCC_min_max) + 1):
    minSCC, maxSCC = SCC_min_max[i-1][0], SCC_min_max[i-1][1]

    if minSCC > k: continue # 그 무리는 포함 시킬 수가 없다.

    for j in range(k + 1):
        dp[i][j] = dp[i-1][j]
        for w in range(minSCC, min(maxSCC+1, j+1)):
            dp[i][j] = max(dp[i][j], dp[i-1][j-w] + w)

print(dp[len(SCC_min_max)][k])
