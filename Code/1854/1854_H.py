import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
#####
n, m, k = map(int, input().split())
arr = [[] for _ in range(n + 1)]    # 지도 정보 저장용 arr
dp = [[INF] * k for _ in range(n + 1)]  # k번째 최단경로 정보를 담을 2차원 리스트

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])   # b까지 가는데 c만큼 걸림
# print(arr)
# print(dp)
# 시작점 초기화
q = []
heapq.heappush(q, [0, 1])
dp[1][0] = 0

# bfs,,,?
while q:
    nowCost, now = heapq.heappop(q)
    for nxt, nxtCost in arr[now]:
        # nxt 노드로 가는 k번째 경로가 nowCost + nxtCost보다 크면 갱신 후 sort하고
        # 갈 수 있는 경로 더 탐색하기 위해 push
        if dp[nxt][k-1] > nowCost + nxtCost:
            dp[nxt][k-1] = nowCost + nxtCost
            dp[nxt].sort()
            heapq.heappush(q, [nowCost + nxtCost, nxt])
    # print(dp)
for i in range(1, n + 1):
    if dp[i][k-1] == INF:
        print(-1)
    else:
        print(dp[i][k-1])
