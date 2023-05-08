import sys
input = sys.stdin.readline

INF = 2501
n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
arr = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(i + 1, n):
        # 현재 정의되어 있는 최소값.
        cur_min = dist[i][j]
        
        for k in range(n):
            if i == k or j == k: continue
            # i에서 j로 k를 거쳐가는 비용.
            to_ikj = dist[i][k] + dist[k][j]

            # print(i, j, k, cur_min, to_ikj)


            # 최단 거리를 줬는데 갱신 여지가 있으면 나가자.
            if to_ikj < cur_min:
                print(-1)
                sys.exit()

            # 값이 더 작은 두 개의 경로로 구성 되어 있음을 의미한다.
            elif to_ikj == cur_min:
                arr[i][j] = 1

s = 0
for i in range(n):
    for j in range(i+1,n):
        if not arr[i][j]:
            s += dist[i][j]
print(s)
        